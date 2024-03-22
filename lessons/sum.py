"""Summing the elements of a list using different loops."""

__author__ = "730661559"


def w_sum(vals: list[float]) -> float:
    """Part 1 - writing the w_sum function."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total
    

def f_sum(vals: list[float]) -> float:
    """Part 2 - calculating the sum of all events in vals."""
    total = 0.0
    for val in vals:
        total += val 
    return total 


def f_range_sum(vals: list[float]) -> float:
    """Part 3 - calculate the sum of all events in vals."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total