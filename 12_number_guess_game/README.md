
# Guess the Number Game

A simple number guessing game where the player has to guess a randomly chosen number between 1 and 100 within a limited number of attempts based on the selected difficulty level.

## Overview

In this game, the computer picks a random number between 1 and 100, and the player tries to guess it. After each guess, the game will indicate whether the guess was too high or too low. The number of guesses allowed depends on the difficulty level:

- **Easy**: 10 attempts
- **Hard**: 5 attempts

The player wins by guessing the correct number within the allowed attempts. Otherwise, the game ends with a loss message.

## How to Play

1. Run the Python script.
2. Choose a difficulty level by typing `easy` or `hard`.
3. Enter your guess when prompted.
4. Follow the hints ("Too High" or "Too Low") until you guess the number or run out of attempts.

## Code Structure

- `level` - prompts the user to select difficulty and sets attempts accordingly.
- `number` - stores a random number between 1 and 100 for the player to guess.
- `game(n)` - recursive function handling each guess and tracking remaining attempts.
  - Takes number of remaining attempts as input.
  - Prints hints and updates attempts.
  - Calls itself until the game is won or attempts run out.

## Running the Game

Run the Python script in a terminal or IDE:

```
python main.py
```

Sample interaction:

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
you have 10 attempts remaining.
Make a guess: 50
Too High.
Guess Again.
...
```
