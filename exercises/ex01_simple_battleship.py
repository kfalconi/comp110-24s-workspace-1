"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730661559"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

user_input1: str = input("Pick a secret boat location between 1 and 4:")
user_number1: int = int(user_input1)

if user_number1 < 1:
    print(f"Error! {user_number1} too low!")
    exit()  # Exit the program 
elif user_number1 > 4:
    print(f"Error! {user_number1} too high!")
    exit()  # Exit the program 

# Part 2: Prompting for Player 2 Input
user_input2: str = input("Guess a number between 1 and 4:")
user_number2: int = int(user_input2)

if user_number2 < 1:
    print(f"Error! {user_number2} too low!")
    exit()  # Exit the program 
elif user_number2 > 4:
    print(f"Error! {user_number2} too high!")
    exit()  # Exit the program 

# Build the emojis
if user_number1 == user_number2:
    if user_number2 == 1:
        print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if user_number2 == 2:
        print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
    if user_number2 == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
    if user_number2 == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{RED_BOX}")
if user_number1 != user_number2:
    if user_number2 == 1:
        print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if user_number2 == 2:
        print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if user_number2 == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")
    if user_number2 == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")

# Part 3: Checking User Input for Match
if user_number1 == user_number2:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")