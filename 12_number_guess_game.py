import random
HARD_LEVEL = 5
EASY_LEVEL = 10
# TODO: printing massage and asking level of difficulty
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(number)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

# TODO: select lives based on difficulty level
lives = 0
if difficulty_level == "easy":
    lives = EASY_LEVEL
elif difficulty_level == "hard":
    lives = HARD_LEVEL

# TODO: create a function that takes input as number, guess number and lives
def check_answer(number, guess_no, lives):
    """this function check whether the user's answer is right or wrong"""
    if guess_no != number:
        if guess_no > number:
            print("Too high\nGuess again")
        else:
            print("Too low\nGuess again")
        if lives == 1:
            print(f"YOU LOST, correct number is {number}")
    elif guess_no == number:
        print(f"you are right, correct number is {number}")
        return 0
    return lives - 1


# TODO: using while loop and asking for number until life is zero
guess_no = 0
while lives > 0:
    print(f"you have  attempts {lives} remaining.")
    guess_no = int(input("make a guess number: "))
    lives = check_answer(number, guess_no, lives)

