"""Mutating functions."""


__author__ = "730661559"


def manual_append(one: list[int], num: int) -> None:
    """Part 1 - manual_append()."""
    one.append(num)


def double(two: list[int]) -> None:
    """Part 2 - double()."""
    index = 0
    while index < len(two):
        two[index] *= 2
        index += 1