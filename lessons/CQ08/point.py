"""CQ08!"""
from __future__ import annotations 
__author__ = "730661559"


class Point:
    """XX."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Create Point class - assigns those as the initial values for the attributes x and y."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutating Method: Point#scale_by."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Instead of mutating, creates a new point."""
        new_x_point = self.x * factor
        new_y_point = self.y * factor
        return Point(new_x_point, new_y_point)