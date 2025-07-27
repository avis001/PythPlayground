import unittest
from findSeriesOfNumbersInSortedArray import findSeries

class TestFindSeries(unittest.TestCase):

    def test_target_not_in_array(self):
        self.assertEqual(findSeries([1, 2, 3, 4, 5], 6), (-1, -1))

    def test_target_in_array_once(self):
        self.assertEqual(findSeries([1, 2, 3, 4, 5], 3), (2, 2))

    def test_target_in_array_multiple_times(self):
        self.assertEqual(findSeries([1, 2, 2, 2, 3, 4, 5], 2), (1, 3))

    def test_target_at_beginning_of_array(self):
        self.assertEqual(findSeries([2, 2, 2, 3, 4, 5], 2), (0, 2))

    def test_target_at_end_of_array(self):
        self.assertEqual(findSeries([1, 2, 3, 4, 5, 5, 5], 5), (4, 6))

    def test_empty_array(self):
        self.assertEqual(findSeries([], 5), (-1, -1))

    def test_all_elements_are_the_same(self):
        self.assertEqual(findSeries([2, 2, 2, 2, 2], 2), (0, 4))

    def test_target_is_first_element_multiple_times(self):
        self.assertEqual(findSeries([2, 2, 3, 4, 5], 2), (0, 1))

    def test_target_is_last_element_multiple_times(self):
        self.assertEqual(findSeries([1, 2, 3, 5, 5], 5), (3, 4))

    def test_single_element_list_target_present(self):
        self.assertEqual(findSeries([5], 5), (0, 0))

    def test_single_element_list_target_absent(self):
        self.assertEqual(findSeries([5], 3), (-1, -1))

    def test_two_elements_both_are_target(self):
        self.assertEqual(findSeries([5, 5], 5), (0, 1))

    def test_two_elements_one_is_target(self):
        self.assertEqual(findSeries([3, 5], 5), (1, 1))

if __name__ == '__main__':
    unittest.main()