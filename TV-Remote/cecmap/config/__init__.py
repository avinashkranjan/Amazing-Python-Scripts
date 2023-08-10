import shlex

from cecmap.commands import Command
from cecmap.keycodes import KEYCODES


class Config:

    def __init__(self, keycodes=KEYCODES):
        self.keycodes = keycodes.copy()
        self.bindings = {'*': {}}
        self.mode = None
        self.modes = []

    def bind(self, keybindings):
        """Set keybindings according to mode."""
        for mode, bindings in keybindings.items():
            if mode != '*':
                if self.mode is None:
                    self.mode = mode
                if mode not in self.modes:
                    self.modes.append(mode)
                    self.bindings[mode] = {}
            self.bindings[mode].update(bindings)

    def keybinding(self, mode, keycode):
        """Get command associated to keycode in current mode."""
        default = self.bindings['*'].get(keycode)
        handler = self.bindings[mode].get(keycode, default)
        return handler

    def load(self, parser, client):
        """
        Load keycodes and keybindings from config parser.

        Returns a new ``Config`` object that is a copy of this config merged
        with the loaded settings.

        See the ``cecmap/config/default.cfg`` file for example.
        """
        keycodes = self.keycodes.copy()
        modes = {}

        if parser.has_section('keycode'):
            section = parser['keycode']
            for name, value in section.items():
                if not value.isnumeric():
                    raise ValueError(
                        "Invalid key code for {}: {!r}".format(name, value))
                keycodes[name] = int(value)

        for section in parser.sections():
            if section.lower().startswith('mode.'):
                mode_name = section[len('mode.'):]
                modes[mode_name] = parser.items(section)
            elif section != 'keycode':
                print("Warning: Unused section in config file:", section)

        all_modes = set(self.modes) | set(modes)
        keybindings = {mode: {} for mode in modes}

        for mode, items in modes.items():
            for key, binding in items:
                command, *args = shlex.split(binding)

                if key.isnumeric():
                    keycode = int(key)
                elif key in keycodes:
                    keycode = keycodes[key]
                else:
                    raise ValueError("Undefined key: {!r}".format(key))

                if command == 'switch' and args and args[0] not in all_modes:
                    raise ValueError("Unknown mode: {!r}".format(args[0]))

                if command in Command.commands:
                    command = Command.commands[command](client, *args)
                else:
                    raise ValueError(
                        "Invalid command: {!r} = {!r}".format(key, binding))

                keybindings[mode][keycode] = command

        config = Config()
        config.keycodes = keycodes
        config.bind(self.bindings)
        config.bind(keybindings)
        return config
