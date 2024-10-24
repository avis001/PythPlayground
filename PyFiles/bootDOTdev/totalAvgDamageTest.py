import unittest
import totalAvgDamage


class Test(unittest.TestCase):
    def testTotalAvgDamage(self):
        self.assertEqual(totalAvgDamage.calculate_damage(5, 5, 15, 20, 55), (100, 20))


# ....totalAvgDamage tests

if __name__ == "__main__":
    unittest.main(verbosity=2)
