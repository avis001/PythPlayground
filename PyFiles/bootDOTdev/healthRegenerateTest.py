import unittest
import healthRegenerate


class Test(unittest.TestCase):
    def testGeneration(self):
        self.assertEqual(healthRegenerate.regenerate(10, 100, 180), 99)

    def testGenerationNoUpdate(self):
        self.assertEqual(healthRegenerate.regenerate(10, 100, 3), 10)

    def testGenerationUpdateByOne(self):
        self.assertEqual(healthRegenerate.regenerate(10, 100, 4), 11)


if __name__ == "__main__":
    unittest.main(verbosity=2)
