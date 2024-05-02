"""Utility functions for working with Linked Lists."""
 
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


# Testing the Node class methods
if __name__ == "__main__":
    # Create a linked list: 0 -> 1 -> 2 -> None
    node_a = Node(0, Node(1, Node(2, None)))

    # Test head() method
    print(node_a.head())  # Output: 0

    # Test tail() method
    print(node_a.tail())  # Output: 1 -> 2 -> None

    # Test last() method
    print(node_a.last())