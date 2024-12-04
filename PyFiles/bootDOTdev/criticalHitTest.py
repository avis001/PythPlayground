import unittest
import criticalHit


class Test(unittest.TestCase):
    def testTotalDamage(self):
        self.assertEqual(criticalHit.calculate_flurry_crit(5, 3), 36)

    def testTotalDamageOneAttack(self):
        self.assertEqual(criticalHit.calculate_flurry_crit(1, 5), 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
