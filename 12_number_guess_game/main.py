from logo import logo
from random import randint

print(logo)
level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
              "\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 10 if level == 'easy' else 5
number = randint(1, 100)


def game(n):
    remaining_attempts = n
    ans = int(input(f"you have {remaining_attempts} attempts remaining.\nMake a guess: "))
    if ans == number:
        print(f"You got it! The answer was {ans}.")
        return None
    elif ans < number:
        print("Too Low.\nGuess Again.")
        remaining_attempts = n-1
    elif ans > number:
        print("Too High.\nGuess Again.")
        remaining_attempts = n - 1
    if remaining_attempts > 0:
        game(remaining_attempts)
    else:
        print("You Lost.\nNo remaining attempts.")


game(attempts)
