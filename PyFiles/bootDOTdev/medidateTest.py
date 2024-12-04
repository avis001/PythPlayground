import unittest
import medidate


class Test(unittest.TestCase):
    def testMedidate(self):
        self.assertEqual(medidate.meditate(0, 10, 3, 0), (9, 0, 0))
        self.assertEqual(medidate.meditate(1000, 1000, 200, 5), (1000, 200, 5))
        self.assertEqual(medidate.meditate(1, 100, 33, 2), (100, 0, 2))
        self.assertEqual(medidate.meditate(0, 10, 0, 2), (10, 46, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
