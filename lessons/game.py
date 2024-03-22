""""Number guessing game."""
from random import randint 

SECRET: int = randint(1,10)
correct: bool = False

while correct == False:  #not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    elif guess > SECRET:
        print(f"Oh no! {guess} too high!")
    elif guess < SECRET:
        print(f"Rayos, truenos y centellas, {guess} too low! El numero es mas grande que el numero de chapes de lele!!!!!")
    else:
        print("Try again!")