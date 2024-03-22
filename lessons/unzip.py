"""Splitting a dictionary into two lists."""

__author__ = "730661559"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Function produces a list of all the keys in the input dictionary."""
    return list(input_dict.keys())


def get_values(input_values: dict[str, int]) -> list[int]:
    """Function produces a list of all the values in the input dictionary."""
    return list(input_values.values())