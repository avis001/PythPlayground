from linkedList import LinkedList

"""
headNode -> fNode -> sNode -> tailNode -> None

we have two pointers one for current and another for previous.

in each iteration we assign current.next to previous, before that we preserve current.next in a temp var.

then we move the pointers,
- prev = current
- current = current.next (use the temp var)

handle head and tail,

if prev is None: tail is the current node
if current.next is None: head is the current node.  

"""


def reverse(ll: LinkedList):
    prev = None
    current = ll.head

    while current:
        if prev is None:
            ll.tail = current

        if current.next is None:
            ll.head = current

        tempNext = current.next
        current.next = prev  # actual reversal
        prev = current
        current = tempNext

    return ll
