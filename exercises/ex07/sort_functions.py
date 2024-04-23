"""Functions that implement sorting algorithms."""

__author__ = "730661559"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    idx_sorted: int = 0
    final: int = len(x) -1
    while idx_sorted < final:
        idx: int = idx_sorted + 1
        current = x[idx]
        while idx > 0 and current < x[idx -1]:
            x[idx] -= 1
        x[idx] = current
        idx_sorted += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    count: int = 0
    while count < len(x):
        idx_min = count
        count_2 = count
        while count_2 < len(x):
            if x[count_2] < x[idx_min]:
                idx_min = count_2
            count_2 += 1
        current = x[count]
        x[count] = x[idx_min]
        x[idx_min] = current
    return None