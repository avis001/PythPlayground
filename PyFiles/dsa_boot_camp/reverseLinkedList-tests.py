

import unittest
from linkedList import LinkedList, Node
from reverseLinkedList import reverse

class TestReverseLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a new LinkedList for each test."""
        self.ll = LinkedList(Node("A"))
        self.ll.append("B")
        self.ll.append("C")
        self.ll.append("D")
        # Expected list: A -> B -> C -> D -> None

    def test_reverse_populated_list(self):
        """Tests reversing a standard list."""
        reverse(self.ll)
        self.assertEqual(str(self.ll), "D -> C -> B -> A -> None\nLength = 4")
        self.assertEqual(self.ll.head.data, "D")

    def test_reverse_single_node_list(self):
        """Tests reversing a list with only one node."""
        single_node_ll = LinkedList(Node("A"))
        reverse(single_node_ll)
        self.assertEqual(str(single_node_ll), "A -> None\nLength = 1")
        self.assertEqual(single_node_ll.head.data, "A")

    def test_reverse_two_node_list(self):
        """Tests reversing a list with two nodes."""
        two_node_ll = LinkedList(Node("A"))
        two_node_ll.append("B")
        reverse(two_node_ll)
        self.assertEqual(str(two_node_ll), "B -> A -> None\nLength = 2")
        self.assertEqual(two_node_ll.head.data, "B")

    def test_double_reverse(self):
        """Tests that reversing a list twice returns it to the original state."""
        original_str = str(self.ll)
        reverse(self.ll)
        self.assertNotEqual(str(self.ll), original_str) # Ensure it changed
        reverse(self.ll)
        self.assertEqual(str(self.ll), original_str) # Ensure it changed back

    def test_new_tail_points_to_none(self):
        """Checks that the new tail (original head) points to None."""
        original_head_data = self.ll.head.data # "A"
        reverse(self.ll)
        
        # The new tail should be the old head
        self.assertEqual(self.ll.tail.data, original_head_data)
        # And its 'next' should be None
        self.assertIsNone(self.ll.tail.next)

    def test_reverse_empty_list(self):
        """Tests reversing a list that has become empty."""
        # Create a list and then make it empty
        ll = LinkedList(Node("X"))
        ll.delNode("X")
        self.assertIsNone(ll.head)

        # Reverse the empty list
        reverse(ll)
        self.assertIsNone(ll.head) # Should still be None
        self.assertIsNone(ll.tail) # Tail should also be None or handled gracefully

if __name__ == '__main__':
    unittest.main(verbosity=2)

