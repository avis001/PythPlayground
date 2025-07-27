import unittest
from numberOfRotations import rotations


class TestNumberOfRotationsUnique(unittest.TestCase):
    def test_no_rotation(self):
        self.assertEqual(rotations([1, 2, 3, 4, 5, 6]), 0)

    def test_random(self):
        self.assertEqual(rotations([4, 5, 1, 2, 3]), 2)

    def test_full_rotation(self):
        self.assertEqual(rotations([2, 3, 4, 5, 6, 1]), 5)

    def test_rotation_in_middle(self):
        self.assertEqual(rotations([4, 5, 6, 1, 2, 3]), 3)

    def test_two_elements_rotated(self):
        self.assertEqual(rotations([2, 1]), 1)

    def test_two_elements_sorted(self):
        self.assertEqual(rotations([1, 2]), 0)

    def test_three_elements_rotation_1(self):
        self.assertEqual(rotations([3, 1, 2]), 1)

    def test_three_elements_rotation_2(self):
        self.assertEqual(rotations([2, 3, 1]), 2)

    def test_large_list_rotation(self):
        self.assertEqual(
            rotations([10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            9,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
