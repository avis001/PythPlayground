
import unittest
from twoSum import two_sum

class TestTwoSum(unittest.TestCase):

    def test_basic_case(self):
        # The sum of 4 and 5 is 9. Their indices are 1 and 2.
        self.assertEqual(sorted(two_sum([2, 4, 5, 7, 8], 9)), [1, 2])

    def test_no_solution(self):
        # No two numbers in the list sum to 15.
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 15), [-1, -1])

    def test_with_negative_numbers(self):
        # The sum of 3 and 4 is 7. Their indices are 0 and 2.
        self.assertEqual(sorted(two_sum([3, -1, 4, 6, 8], 7)), [0, 2])

    def test_with_zero_in_list(self):
        # The sum of 0 and 5 is 5. Their indices are 2 and 3.
        self.assertEqual(sorted(two_sum([1, 2, 0, 5], 5)), [2, 3])

    def test_target_sum_is_zero(self):
        # The sum of -5 and 5 is 0. Their indices are 1 and 3.
        self.assertEqual(sorted(two_sum([1, -5, 2, 5], 0)), [1, 3])

    def test_with_duplicate_numbers(self):
        # The sum of 5 and 5 is 10. Their indices are 2 and 3.
        self.assertEqual(sorted(two_sum([1, 2, 5, 5, 6], 10)), [2, 3])

    def test_empty_list(self):
        # An empty list should return [-1, -1].
        self.assertEqual(two_sum([], 10), [-1, -1])

    def test_two_elements_sum_to_target(self):
        # The sum of 1 and 9 is 10. Their indices are 0 and 1.
        self.assertEqual(sorted(two_sum([1, 9], 10)), [0, 1])

    def test_first_and_last_elements(self):
        # The sum of 11 and 20 is 31. Their indices are 0 and 4.
        self.assertEqual(sorted(two_sum([11, 2, 7, 15, 20], 31)), [0, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
