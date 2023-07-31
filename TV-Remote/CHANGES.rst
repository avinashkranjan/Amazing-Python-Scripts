Changes
-------

v1.0.0
~~~~~~
Date: 28.11.2021

- rename to cecmap
- switch default keybindings for F1 (blue) and F4 (yellow)
- add keycodes for all user control codes defined by CEC


v0.0.5
~~~~~~
Date: 27.11.2021

- fix KeyError if a motion-bound key was already pressed before starting
  picec but released afterwards
- set/decrease notification timeout to 3s
- move code to picec.cli submodule
- remove ability to load .py config files
- add ability to load .cfg config files
- add ability to reload config on the fly using SIGUSR1
- add ability to merge config from multiple .cfg files
- document config format


v0.0.4
~~~~~~
Date: 26.11.2021

- fix: TypeError: __init__() missing 1 required positional argument: 'app_name'
- fix: AttributeError: 'dict' object has no attribute 'setup'
- fix: AttributeError: module 'os' has no attribute 'setpgrgp'


v0.0.3
~~~~~~
Date: 25.11.2021

- spawn subprocesses in new process group
  (to avoid tearing them down with us when we are stopped)
- execute via ``bash -l`` in .service file to ensure PATH customizations are
  available. This may fix an error when autostarting the service, and will
  be useful for launching locally installed applications.
- move code to package structure
- use entrypoint for creating the executable
- rename executable from ``picec.py`` to ``picec``
- add command line option to change config
  (undocumented so far, and the API will change!)
- load config from ``~/.config/picec/config.py`` if exists
- simplify config
- bind ``matchbox-keyboard`` to red button in mouse mode
- add notification about mode changes using notify2


v0.0.2
~~~~~~
Date: 22.11.2021

- replace xdotool by ``pynput``
- make .service restart on failure


v0.0.1
~~~~~~
Date: 22.11.2021

Initial prototype:

- hard coded keybindings
- for LG TV with magic remote
- "mouse" and "keyboard" mode for controlling the mouse or cursor keys
- based on xdotool
- includes an example .service file
