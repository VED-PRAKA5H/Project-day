# Higher Lower Game

A fun interactive guessing game where the player predicts which celebrity has more Instagram followers. The player continues guessing until a wrong answer ends the game.

## Overview

This game challenges the player to guess whether the next celebrity has more or fewer Instagram followers compared to the current one. A random pair of celebrities is presented with some details like name, profession, and country. The player chooses between "A" or "B" to indicate who they believe has a higher follower count. The game keeps track of the player's score for consecutive correct guesses.

## How to Play

1. Run the script.
2. The game will display two celebrities with their basic info.
3. Guess who has more Instagram followers by typing `A` or `B`.
4. If the guess is correct, the score increments and the game continues with the next comparison.
5. If the guess is incorrect, the game ends and the final score is displayed.

## Code Structure

- `random_celeb(n)`: Generates a random celebrity index different from the given index to avoid comparing the same celebrity.
- `compare_followers(pos1, pos2)`: Compares the follower counts of two celebrities and returns `True` if the first has more followers.
- `higher_lower()`: Main game loop that:
  - Picks two distinct random celebrities.
  - Presents info for comparison.
  - Takes user input and checks correctness.
  - Updates the score and repeats or ends the game.

## Requirements

- Python 3.x
- `random` module (standard library)
- Custom modules/files:
  - `art.py` providing `logo1`, `logo2`
  - `list.py` containing `data_of_celebs` list with celebrity info and follower counts

## Running the Game

Run the Python script in a terminal or IDE:

```
python main.py
```

Example game interaction:

```
Compare A: John Doe, a actor from USA.
[logo2]
Against B: Jane Smith, a singer from UK.
Who has more followers? Type 'A' or 'B': a
you're right! and your current score 1
...
```
