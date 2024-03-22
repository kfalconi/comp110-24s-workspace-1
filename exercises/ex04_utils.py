"""EX04 - Utils."""

__author__ = "730661559"


def all(nums: list[int], match: int) -> bool:
    """Part 1 - All function."""
    for num in nums:
        if num != match:
            return False 
    return True if nums else False


def max(nums: list[int]) -> int:
    """Parte 2 - Return max for the largest number, if empty, return ValueError."""
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List.")
    num_max = nums[0]
    for num in nums:
        if num > num_max:
            num_max = num
    return num_max


def is_equal(list1: list[int], list2: list[int]) -> int:
    """Return true if all elements at all indexes are equal."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate the first list of int values by appending the second lists values to the end of it."""
    list1.extend(list2)