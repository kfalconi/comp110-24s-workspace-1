""""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730661559"

user_input: str = input("Pick a secret boat location between 1 and 4:")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if a number is =>0, print "TOO small"
if user_number <=0 :
    print(f"Error! {user_number} too small!")
else: # user_number >= 4
    if user_number >= 5 :
        print(f"Error! {user_number} too high!")
    else: 
        user_input2: str = input("Pick a secret boat location between 1 and 4:")
        print(type(user_input2))
        user_number2: int = int(user_input2)
        print(type(user_number2))


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if user_number2 <=0 :
    print(f"Error! {user_number2} too small!")
else: # user_number >= 4
    if user_number2 >= 5 :
        print(f"Error! {user_number2} too high!")
    else: 
        if user_number == user_number2 :
            if user_number2 == 1 :
                print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
                print("Correct! You hit the ship.")
            else: 
                if user_number2 == 2 :
                    print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
                    print("Correct! You hit the ship.")
                else: 
                    if user_number == 3 :
                        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
                        print("Correct! You hit the ship.")
                    else: 
                        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{RED_BOX}")
                        print("Correct! You hit the ship.")

        else:
            if user_number2 == 1 :
                print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
                print("Incorrect! You missed the ship.")
            else: 
                if user_number2 == 2 :
                    print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
                    print("Incorrect! You missed the ship.")
                else: 
                    if user_number == 3 :
                        print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")
                        print("Incorrect! You missed the ship.")
                    else: 
                        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
                        print("Incorrect! You missed the ship.")


