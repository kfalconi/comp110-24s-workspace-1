""""EX02 - One shot battleship"""

__author__ = "730661559"
from random import randint 

secret_row: int = randint(1,4)
secret_column: int = randint(1,4)
grid_size: int = 4

correct: bool = False 

guess_row: int = int(input("Guess a row: "))
while guess_row < 1 or guess_row > grid_size:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))


guess_column: int = int(input("Guess a column: "))
while guess_column < 1 or guess_column > grid_size:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"