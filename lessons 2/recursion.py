"""Recursion Challenge Question."""

__author__ = "730661559"


def f(n: int, k: int) -> int:
    """Recursion to multiply both integers."""
    if n == 0:
        return 0
    else:
        n *= k
        return n