import argparse
import os
import signal
import time
from configparser import ConfigParser
from importlib.resources import is_resource, read_text
from queue import Queue, Empty

from tv.config import Config
from tv.device import Keyboard, Mouse
from tv.notify import Notify


class Clock:

    def __init__(self):
        self.prev = time.perf_counter()

    def __call__(self):
        now = time.perf_counter()
        delta = now - self.prev
        self.prev = now
        return delta


def reload(client, *config_files):
    """Reload config."""
    if not config_files:
        config_home = (
            os.environ.get('XDG_CONFIG_HOME') or
            os.path.expanduser('~/.config'))
        if os.path.exists(os.path.join(config_home, "tv.cfg")):
            config_files = [os.path.join(config_home, "tv.cfg")]
        elif os.path.exists('/etc/tv.cfg'):
            config_files = ['/etc/tv.cfg']
        else:
            config_files = ['default']

    parser = ConfigParser()
    for config_file in config_files:
        print("Loading config file:", config_file)
        resource = ('tv.config', config_file + '.cfg')
        if '/' not in config_file and is_resource(*resource):
            text = read_text(*resource)
        else:
            with open(config_file) as f:
                text = f.read()
        parser.read_string(text)

    client.reset(Config().load(parser, client))


def main(args=None):
    args = parse_args(args)
    timestep = 0.01
    client = Client()
    signal.signal(signal.SIGUSR1, lambda *_: reload(client, *args.config))
    reload(client, *args.config)

    print("Initializing...")
    client.connect()
    print("Ready")
    clock = Clock()
    while True:
        timeout = timestep if any(d.active for d in client.devices) else None
        events = client.recv(timeout)
        time_delta = clock()
        for device in client.devices:
            if device.active:
                device.dispatch(time_delta)
        for event in events:
            client.dispatch(*event)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default=[], action='append')
    return parser.parse_args(args)


class Client:

    def __init__(self):
        self.config = Config()
        self.mode = None
        self.events = Queue()
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.devices = [self.mouse, self.keyboard]
        self.notify = Notify("tv", timeout=3000)

    def reset(self, config):
        self.config = config
        if self.mode not in config.modes:
            self.mode = config.mode

    def switch(self, mode=None):
        """Switch to the given or the next mode."""
        if mode is None:
            current = self.config.modes.index(self.mode)
            mode = self.config.modes[(current + 1) % len(self.config.modes)]
        if self.mode != mode:
            self.mode = mode
            self.notify("Mode: {}".format(mode))

    def connect(self):
        cec.init()
        cec.set_active_source()
        cec.add_callback(self.on_keypress, cec.EVENT_KEYPRESS)

    def on_keypress(self, event, keycode, duration):
        self.events.put((event, keycode, duration))

    def recv(self, timeout):
        events = []
        try:
            events.append(self.events.get(timeout=timeout))
            while True:
                events.append(self.events.get_nowait())
        except Empty:
            return events

    def dispatch(self, event, keycode, duration):
        handler = self.config.keybinding(self.mode, keycode)
        if handler:
            handler(duration)


if __name__ == '__main__':
    main()
