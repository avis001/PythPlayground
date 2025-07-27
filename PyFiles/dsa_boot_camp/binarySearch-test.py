import unittest
from binarySearch import search


class TestBinarySearch(unittest.TestCase):
    def test_target_present(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 3), 2)

    def test_target_not_present(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        self.assertEqual(search([], 5), -1)

    def test_target_is_first_element(self):
        self.assertEqual(search([10, 20, 30, 40], 10), 0)

    def test_target_is_last_element(self):
        self.assertEqual(search([10, 20, 30, 40], 40), 3)

    def test_list_with_duplicates(self):
        self.assertIn(search([1, 2, 2, 2, 3], 2), [1, 2, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(search([-5, -2, 0, 3, 8], -2), 1)

    def test_list_with_zero(self):
        self.assertEqual(search([-5, -2, 0, 3, 8], 0), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
