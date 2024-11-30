import unittest
import playerStatus


class Test(unittest.TestCase):
    def testPlayerStatusDead(self):
        self.assertEqual(playerStatus.player_status(-4), "dead")

    def testPlayerStatusInjured(self):
        self.assertEqual(playerStatus.player_status(5), "injured")

    def testPlayerStatusHealthy(self):
        self.assertEqual(playerStatus.player_status(8), "healthy")


if __name__ == "__main__":
    unittest.main(verbosity=2)
