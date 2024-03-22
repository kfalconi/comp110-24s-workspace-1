"""EX02 - One shot battleship."""

__author__ = "730661559"

GRID_SIZE: int = 4
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

secret_row: int = 3
secret_column: int = 2

# inputing the row
guess_row = int(input("Guess a row: "))
while guess_row < 1 or guess_row > GRID_SIZE:
    guess_row = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
    
# inputing the column
guess_column = int(input("Guess a column: "))
while guess_column < 1 or guess_column > GRID_SIZE:
    guess_column = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))

# inserting the row of emojis
row = 1
while row <= GRID_SIZE:
    emoji_row = ""
    column = 1
    while column <= GRID_SIZE:
        if row == guess_row and column == guess_column:
            emoji = RED_BOX if row == secret_row and column == secret_column else WHITE_BOX
        else:
            emoji = BLUE_BOX
        emoji_row += emoji 
        column += 1
    print(emoji_row)
    row += 1

# final message
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column and guess_row != secret_row:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")