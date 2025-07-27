"""
How to pass a linkedList as an argument? Just pass in the linkedList instance.

What do we need?
1. A node class with data and a pointer to the next node.
2. A LinkedList class - headNode
3. Functions in the linked List ( as suggested by gemini )
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


class LinkedList:
    # Node argument cannot be a linkedList of Nodes. That would lead to incorrect count.
    def __init__(self, head: Node):
        self.head = head
        self.tail = head
        self.count = 1

    # Dunder Functions
    def __str__(self):
        if not self.head:
            return "Empty LinkedList"

        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes) + " -> None" + f"\nLength = {self.count}"

    def __repr__(self):
        return f"LinkedList(head={repr(self.head)})"

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

    # Insertions

    # Insert at the end
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    # Insert at the beginig
    # head -> Node1 -> None
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    # Insert after a given Node
    # 1. Find the node 2. newNode.next = previousNode.next | previousNode.next = newNode
    def insertAfterNode(self, prevNodeData, data):
        newNode = Node(data)
        previousNode = None

        current = self.head
        while current:
            if current.data == prevNodeData:
                previousNode = current
                break
            else:
                current = current.next

        if previousNode is None:
            raise ValueError("Previous Node isn't part of the linked list.")

        newNode.next = previousNode.next
        previousNode.next = newNode

        if previousNode == self.tail:
            self.tail = newNode

        self.count += 1

    # Insert at a position [ insert at 0 is just prepend and insert at len of list is append ]
    def insertAtPosition(self, position, data):
        if position == 0:
            self.prepend(data)
        elif position == self.count:
            self.append(data)
        else:
            newNode = Node(data)
            currentPosition = 0
            current = self.head

            while current:
                if currentPosition == position - 1:
                    newNode.next = current.next
                    current.next = newNode
                    self.count += 1
                    break
                else:
                    currentPosition += 1
                    current = current.next

    # Deletions

    # Delete First
    # head -> fNode -> sNode -> None
    def delFirst(self):
        head = self.head
        self.head = head.next
        self.count -= 1

    # Delete Last
    def delLast(self):
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next

        prev.next = None
        self.tail = prev
        self.count -= 1

    # Delete a specific node ( if there are dups removes the first instance of the node )
    def delNode(self, data):
        prev = None
        current = self.head
        deleted = False

        while current:
            if current.data == data:
                if prev is None:
                    self.delFirst()
                else:
                    prev.next = current.next

                    if current == self.tail:
                        self.tail = prev
                    self.count -= 1

                deleted = True
                break
            else:
                prev = current
                current = current.next

        if not deleted:
            raise ValueError("Data not in List. Hence not deleted.")

    # Delete the node at a given position.
    def delAtPosition(self, position):
        if position == 0:
            self.delFirst()
        elif position == self.count - 1:
            self.delLast()
        else:
            prev = self.head
            current = self.head.next
            counter = 1
            deleted = False

            while current:
                if counter == position:
                    prev.next = current.next
                    self.count -= 1
                    deleted = True
                    break
                else:
                    prev = current
                    current = current.next
                    counter += 1

            if not deleted:
                raise ValueError("Position outta range.")
