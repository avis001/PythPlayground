import unittest
import combactAdvantage


class Tests(unittest.TestCase):
    def testAdvantage(self):
        self.assertTrue(
            combactAdvantage.combat_evaluation(140, 100), (True, False, False)
        )

    def testDisadvantage(self):
        self.assertTrue(
            combactAdvantage.combat_evaluation(140, 150), (False, True, False)
        )

    def testEvenlyMatched(self):
        self.assertTrue(
            combactAdvantage.combat_evaluation(140, 140), (False, False, True)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
