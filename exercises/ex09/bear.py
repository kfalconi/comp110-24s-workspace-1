"""File to define Bear class."""

__author__ = "730661559"


class Bear:
    """Hello Bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize Bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Is the bear hungry or full?"""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increasing bears with yummy fish."""
        self.hunger_score += num_fish
        return None