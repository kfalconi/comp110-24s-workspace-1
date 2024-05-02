"""File to define Fish class."""

__author__ = "730661559"


class Fish:
    """Starting Fish."""
    age: int

    def __init__(self):
        """Start."""
        self.age = 0
        return None
    
    def one_day(self):
        """Add 1."""
        self.age += 1
        return None