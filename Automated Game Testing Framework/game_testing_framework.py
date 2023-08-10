import unittest


class Game:
    def __init__(self):
        self.is_running = False
        self.score = 0

    def start(self):
        self.is_running = True
        return "Game started."

    def play(self, action):
        if self.is_running:
            if action == "move_forward":
                self.score += 10
            elif action == "attack":
                self.score += 20
            elif action == "use_item":
                self.score += 5
            return f"Performed action: {action}"
        else:
            return "Game is not running."

    def quit(self):
        self.is_running = False
        return "Game quit."


class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.start()

    def test_start(self):
        self.assertTrue(self.game.is_running)
        self.assertEqual(self.game.start(), "Game started.")

    def test_actions(self):
        actions = ["move_forward", "attack", "use_item"]
        for action in actions:
            with self.subTest(action=action):
                result = self.game.play(action)
                self.assertIn(action, result)
                self.assertGreaterEqual(self.game.score, 0)

    def test_quit(self):
        self.assertTrue(self.game.is_running)
        self.assertEqual(self.game.quit(), "Game quit.")
        self.assertFalse(self.game.is_running)

    def test_non_running_actions(self):
        self.game.quit()
        result = self.game.play("move_forward")
        self.assertEqual(result, "Game is not running.")


if __name__ == "__main__":
    unittest.main()
