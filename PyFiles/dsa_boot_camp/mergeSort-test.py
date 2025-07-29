import unittest
from mergeSort import sort


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort([1]), [1])

    def test_unsorted_list(self):
        self.assertEqual(sort([3, 1, 2]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(sort([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_sorted_list(self):
        self.assertEqual(sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted_list(self):
        self.assertEqual(sort([3, 2, 1]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
