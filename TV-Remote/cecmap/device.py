from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key

__all__ = [
    'Key',
    'Button',
    'Mouse',
    'Keyboard',
]


class Device:

    active = False

    def dispatch(self, seconds_passed):
        pass


class Mouse(Device):

    def __init__(self, speed=200):
        self.speed = speed
        self.controller = MouseController()
        self.active = set()
        self.dx = {Key.left: -1, Key.right: 1}
        self.dy = {Key.up: -1, Key.down: 1}
        self.pos0 = (0, 0)
        self.pos1 = self.pos0

    @property
    def button(self):
        return (self.press, self.release)

    def press(self, button):
        self.controller.press(button)

    def release(self, button):
        self.controller.release(button)

    def scroll(self, dx, dy):
        self.controller.scroll(dx, dy)

    @property
    def motion(self):
        return (self.start_motion, self.stop_motion)

    def start_motion(self, key):
        self.active.add(key)

    def stop_motion(self, key):
        self.active.discard(key)

    def dispatch(self, delta):
        dx = sum([self.dx.get(key, 0) for key in self.active])
        dy = sum([self.dy.get(key, 0) for key in self.active])
        x0, y0 = self.pos0
        x1, y1 = self.pos1
        x1 += dx * delta * self.speed
        y1 += dy * delta * self.speed
        x2 = round(x1)
        y2 = round(y1)
        self.pos0 = (x2, y2)
        self.pos1 = (x1, y1)
        if x2 != x0 or y2 != y0:
            self.controller.move(x2 - x0, y2 - y0)


class Keyboard(Device):

    def __init__(self):
        self.controller = KeyboardController()

    @property
    def key(self):
        return (self.press, self.release)

    def press(self, key):
        self.controller.press(key)

    def release(self, key):
        self.controller.release(key)

    def dispatch(self, delta):
        pass
