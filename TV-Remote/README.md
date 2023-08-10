TV-Controller
======

Install
-------

You can install *TV-Controller* as user or root:

**as user:**

::

    pip3 install --user cecmap

Also, make sure to add ``~/.local/bin`` to your PATH.


**as root:**

::

    sudo pip3 install cecmap

In order to see notifications when switching modes, it's also necessary to
have a notification daemon installed. I recommend ``xfce4-notifyd``::

    sudo apt install xfce4-notifyd

I also recommend installing an onscreen keyboard, e.g.::

    sudo apt install matchbox-keyboard


Usage
-----

Launch::

    cecmap

    # or:

    python -m tv


Running as service
------------------

Enable running at startup::

    systemctl --user enable tv

Start as service::

    systemctl --user start tv


Default keybindings
-------------------
The default keybindings are as follows:

.. list-table::
    :header-rows: 1

    * - Key
      - *Mouse* mode
      - *Keyboard* mode

    * - 🔵 F1 blue
      - switch mode
      - switch mode
    * - 🔴 F2 red
      - launch ``matchbox-keyboard``
      - ``<Win>``
    * - 🟢 F3 green
      - mouse wheel up
      - launch kodi
    * - 🟡 F4 yellow
      - mouse wheel down
      - launch ``chromium-browser``

    * - ⬆ up
      - move cursor up
      - ``<up>``
    * - ⬇ down
      - move cursor down
      - ``<down>``
    * - ⬅ left
      - move cursor left
      - ``<left>``
    * - ➡ right
      - move cursor right
      - ``<right>``

    * - 🆗 select
      - left click
      - ``<enter>``
    * - ▶ play
      - middle click
      - ``<media_play_pause>``

    * - ⏸ pause
      - right click
      - ``<media_play_pause>``
    * - ↩ exit
      - ``<esc>``
      - ``<esc>``


Configuration
-------------

*cecmap* uses a simple config format to set keycodes and keybindings. The
config to be used can be specified on the command line using the ``-c
FILE.cfg`` option. The format is as follows:

.. code-block:: cfg

    [keycode]
    KEY = <NUMBER>
    ...

    [mode.NAME]
    KEY = <command> [<args>...]
    ...

e.g.:

.. code-block:: cfg

    [keycode]
    left = 123
    yellow = 321
    ...

    [mode.Keyboard]
    left = key left
    yellow = launch kodi
    ...
