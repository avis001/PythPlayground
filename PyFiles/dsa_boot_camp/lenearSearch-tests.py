import unittest
import lenearSearch

class TestLinearSearch(unittest.TestCase):

    def test_target_present(self):
        """Test case for when the target is in the list."""
        self.assertTrue(lenearSearch.search([1, 2, 3, 4, 5], 3))

    def test_target_not_present(self):
        """Test case for when the target is not in the list."""
        self.assertFalse(lenearSearch.search([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertFalse(lenearSearch.search([], 5))

    def test_target_is_first_element(self):
        """Test case for when the target is the first element."""
        self.assertTrue(lenearSearch.search([10, 20, 30, 40], 10))

    def test_target_is_last_element(self):
        """Test case for when the target is the last element."""
        self.assertTrue(lenearSearch.search([10, 20, 30, 40], 40))

    def test_list_with_duplicates(self):
        """Test case for a list with duplicate elements."""
        self.assertTrue(lenearSearch.search([1, 2, 2, 3, 4], 2))

    def test_list_with_negative_numbers(self):
        """Test case for a list containing negative numbers."""
        self.assertTrue(lenearSearch.search([-1, -5, 2, 8], -5))

    def test_list_with_zero(self):
        """Test case for a list containing zero."""
        self.assertTrue(lenearSearch.search([1, 0, 5, -3], 0))

if __name__ == "__main__":
    unittest.main(verbosity=2)