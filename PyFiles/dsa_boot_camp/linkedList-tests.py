import unittest
from linkedList import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up a new LinkedList for each test."""
        # Per user, LinkedList cannot be initialized empty.
        # Start with a head node.
        self.ll = LinkedList(Node("A"))
        self.ll.append("B")
        self.ll.append("C")
        # Expected list: A -> B -> C -> None, Length = 3

    def test_initialization_and_str(self):
        self.assertEqual(str(self.ll), "A -> B -> C -> None\nLength = 3")

    def test_append(self):
        self.ll.append("D")
        self.assertEqual(str(self.ll), "A -> B -> C -> D -> None\nLength = 4")

    def test_prepend(self):
        self.ll.prepend("Z")
        self.assertEqual(str(self.ll), "Z -> A -> B -> C -> None\nLength = 4")
        self.assertEqual(self.ll.head.data, "Z")

    def test_insert_after_node(self):
        self.ll.insertAfterNode("B", "X")
        self.assertEqual(str(self.ll), "A -> B -> X -> C -> None\nLength = 4")
        # Test inserting after the last node
        self.ll.insertAfterNode("C", "Y")
        self.assertEqual(str(self.ll), "A -> B -> X -> C -> Y -> None\nLength = 5")
        # Test error on non-existent node
        with self.assertRaises(ValueError):
            self.ll.insertAfterNode("M", "N")

    def test_insert_at_position(self):
        # Insert in the middle
        self.ll.insertAtPosition(1, "X")
        self.assertEqual(str(self.ll), "A -> X -> B -> C -> None\nLength = 4")
        # Insert at the beginning
        self.ll.insertAtPosition(0, "Y")
        self.assertEqual(str(self.ll), "Y -> A -> X -> B -> C -> None\nLength = 5")
        # Insert at the end
        self.ll.insertAtPosition(5, "Z")
        self.assertEqual(str(self.ll), "Y -> A -> X -> B -> C -> Z -> None\nLength = 6")

    def test_del_first(self):
        self.ll.delFirst()
        self.assertEqual(str(self.ll), "B -> C -> None\nLength = 2")
        self.assertEqual(self.ll.head.data, "B")

    def test_del_last(self):
        self.ll.delLast()
        self.assertEqual(str(self.ll), "A -> B -> None\nLength = 2")
        # Test on a list with two elements
        self.ll.delLast()
        self.assertEqual(str(self.ll), "A -> None\nLength = 1")

    def test_del_node(self):
        # Delete from the middle
        print(str(self.ll))
        self.ll.delNode("B")
        self.assertEqual(str(self.ll), "A -> C -> None\nLength = 2")
        # Delete the head
        self.ll.delNode("A")
        self.assertEqual(str(self.ll), "C -> None\nLength = 1")
        # Delete the remaining node, resulting in an empty list
        self.ll.delNode("C")
        self.assertEqual(str(self.ll), "Empty LinkedList")
        # Test error on non-existent node
        with self.assertRaises(ValueError):
            self.ll.delNode("Z")

    def test_del_at_position(self):
        # Delete from the middle
        self.ll.delAtPosition(1)
        self.assertEqual(str(self.ll), "A -> C -> None\nLength = 2")
        # Delete the head
        self.ll.delAtPosition(0)
        self.assertEqual(str(self.ll), "C -> None\nLength = 1")
        # Reset and delete the tail
        self.setUp()
        self.ll.delAtPosition(2)
        self.assertEqual(str(self.ll), "A -> B -> None\nLength = 2")
        # Test error on out-of-range position
        with self.assertRaises(ValueError):
            self.ll.delAtPosition(10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
