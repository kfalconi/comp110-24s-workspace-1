"""CQ10 - The Last Dance!"""

from __future__ import annotations
 
__author__ = "730661559"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None = None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
    
    def head(self) -> int:
        """Return the data of the first element in the linked list."""
        return self.data

    def tail(self) -> Node | None:
        """Return a new linked list excluding the head element."""
        return self.next

    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data


def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index < 0:
        raise IndexError("Negative index is not allowed.")
    if index == 0:
        return head.data
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    return _max_recursive(head, head.data)


def _max_recursive(node: Node | None, current_max: int) -> int:
    """Helper function to recursively find the maximum value."""
    if node is None:
        return current_max
    if node.data > current_max:
        current_max = node.data
    return _max_recursive(node.next, current_max)


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values as the input list."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is scaled by the factor."""
    if head is None:
        return None
    return Node(head.data * factor, scale(head.next, factor))