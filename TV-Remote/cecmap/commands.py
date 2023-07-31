import os
import subprocess

from pynput.mouse import Button
from pynput.keyboard import Key, KeyCode


SCROLL_DIR = {
    'up': (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0),
}

MOTION_DIR = {
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right,
}


class _Button:
    def __init__(self, button):
        self.value = button


class Command:

    """Action to execute as response to a CEC input."""

    def __init__(self, name, press, release, *args):
        self.name = name
        self.press = press
        self.release = release
        self.args = args

    def __call__(self, duration):
        """Execute the command."""
        if duration == 0:
            if self.press:
                self.press(*self.args)
        else:
            if self.release:
                self.release(*self.args)

    def __repr__(self):
        return '{}({})'.format(self.name, ', '.join(map(str, self.args)))

    @classmethod
    def launch(cls, client, *argv):
        """Launch and forget an application."""
        return cls("launch", launch, None, *argv)

    @classmethod
    def toggle(cls, client, *argv):
        """Start/stop an application."""
        return cls("toggle", toggle, None, *argv)

    @classmethod
    def key(cls, client, name):
        """Type a keyboard key, see ``pynput.keyboard.Key`` for valid keys."""
        if name.isnumeric():
            key = KeyCode.from_vk(int(name))
        elif name.startswith('@') and len(name) == 2:
            key = KeyCode.from_char(name[1])
        elif is_public(Key, name):
            key = getattr(Key, name)
        else:
            raise ValueError("Invalid key name: {!r}".format(name))
        kbd = client.keyboard
        return cls("key", kbd.press, kbd.release, key)

    @classmethod
    def button(cls, client, name):
        """Click a mouse button (left/middle/right)."""
        if name.isnumeric():
            button = _Button(int(name))
        elif is_public(Button, name):
            button = getattr(Button, name)
        else:
            raise ValueError("Invalid button name: {!r}".format(name))
        mouse = client.mouse
        return cls("button", mouse.press, mouse.release, button)

    @classmethod
    def scroll(cls, client, dir, ticks='1'):
        """Scroll the mouse wheel (up/down/left/right) the specified number of
        ticks."""
        if dir not in SCROLL_DIR:
            raise ValueError("Invalid scroll direction: {!r}".format(dir))
        if not ticks.isnumeric():
            raise ValueError("Invalid scroll tick number: {!r}".format(ticks))
        dx, dy = SCROLL_DIR[dir]
        ticks = int(ticks)
        mouse = client.mouse
        return cls("scroll", mouse.scroll, None, dx * ticks, dy * ticks)

    @classmethod
    def motion(cls, client, dir):
        """Move the mouse along given direction (up/down/left/right)."""
        if dir not in MOTION_DIR:
            raise ValueError("Invalid move direction: {!r}".format(dir))
        motion = MOTION_DIR[dir]
        mouse = client.mouse
        return cls("motion", mouse.start_motion, mouse.stop_motion, motion)

    @classmethod
    def switch(cls, client, mode=None):
        """Switch mode to the next mode. Optional argument allows specifying a
        specific mode to switch to."""
        return cls("switch", client.switch, None, mode)


Command.commands = {
    'launch': Command.launch,
    'toggle': Command.toggle,
    'key':    Command.key,
    'button': Command.button,
    'scroll': Command.scroll,
    'motion': Command.motion,
    'switch': Command.switch,
}


def is_public(obj, attr):
    return not attr.startswith('_') and hasattr(obj, attr)


def launch(*args, **kwargs):
    """
    Launch and forget process.

    Will be detached from current process group to avoid it being stopped
    when we are killed.
    """
    return subprocess.Popen(args, preexec_fn=os.setpgrp, **kwargs)


# Keep global score of started processes, so that toggles defined in different
# modes always refer to the same process:
_procs = {}


def toggle(*args, **kwargs):
    """Start process. If already running, terminate."""
    if args in _procs:
        _procs.pop(args).terminate()
    else:
        _procs[args] = launch(*args, **kwargs)
