import unittest
from numberOfRotations import rotations


class TestNumberOfRotationsRepeating(unittest.TestCase):
    def test_repetition(self):
        self.assertEqual(rotations([6, 6, 6, 6, 5, 6]), 4)

    def test_repetition_v1(self):
        self.assertEqual(rotations([6, 5, 6, 6, 6, 6]), 1)

    def test_list_with_duplicates_rotated(self):
        self.assertEqual(rotations([5, 5, 5, 1, 2, 3, 4, 5]), 3)

    def test_list_with_duplicates_at_end(self):
        self.assertEqual(rotations([3, 4, 1, 2, 3, 3]), 2)

    def test_list_with_all_same_elements(self):
        self.assertEqual(rotations([2, 2, 2, 2, 2]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
