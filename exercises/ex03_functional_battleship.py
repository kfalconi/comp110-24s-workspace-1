"""EX03 Functional Battleship."""

import random

__author__ = "730661559"

WHITE_BOX: str = "\U00002B1C"
RED_BOX: str = "\U0001F7E5"
BLUE_BOX: str = "\U0001F7E6"


def input_guess(size: int, guess_type: str) -> int:
    """Inputing the guesses - Step 1."""
    guess = int(input(f"Guess a {guess_type}: "))
    while guess < 1 or guess > size:
        print(f"The grid is only {size} by {size}. Try again: ")
        guess = int(input(f"Guess a {guess_type}: "))
    return guess


def input_guess(size: int, spec: str) -> int:
    """1st step of guesses."""
    assert spec in ["row", "column"], "spec must be 'row' or 'column'"
    guess = int(input(f"Guess a {spec}: "))
    while guess < 1 or guess > size:
        print(f"The grid is only {size} by {size}. Try again: ")
        guess = int(input(f"Guess a {spec}: "))
    return guess

def print_grid(size: int, row_guess: int, col_guess: int, correct: bool) -> None:
    """Printing the grid - Step 2."""
    row = 1
    while row <= size:
        col = 1
        while col <= size:
            if row == row_guess and col == col_guess:
                print(RED_BOX if correct else WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
            col += 1
        print()
        row += 1


def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Returning correct row and column - Step 3."""
    return secret_row == row_guess and secret_col == col_guess


def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Main grid, giving hints - Step 4."""
    turns = 5
    turn = 1
    while turn <= turns:
        print(f"=== Turn {turn}/{turns} ===")
        row_guess = input_guess(grid_size, "row")
        col_guess = input_guess(grid_size, "column")
        is_correct = correct_guess(secret_row, secret_col, row_guess, col_guess)
        print_grid(grid_size, row_guess, col_guess, is_correct)
        if is_correct:
            print(f"Hit!\nYou won in {turn}/{turns} turns!")
            return
        else:
            print("Miss!")
        turn += 1
    print(f"X/{turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size = 4
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))