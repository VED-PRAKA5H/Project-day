# Hangman Game

A classic word-guessing game built with Python where players guess letters to reveal a hidden word before running out of lives.

### How It Works  
1. The game displays a welcome logo and selects a random secret word from a predefined list.  
2. The player guesses one letter at a time.  
3. If the guessed letter is in the word, the game reveals all instances of that letter.  
4. If the guess is incorrect, the player loses a life.  
5. The game continues until the player either guesses the whole word or runs out of lives.  
6. The hangman stages visually update with each wrong guess.

### Example Gameplay  
```
Welcome to Hangman!  
_ _ _ _ _ _ _  
>Guess a letter: e  
_ e _ _ _ _ _  
Oops! That letter is not in the word.  
You have 5 lives remaining.  
[Hangman stage graphic]  
```

### How to Play  
- Run the script using Python:  
```
python main.py
```
- Enter your letter guesses as prompted.  

### Requirements  
- Python 3.x  
- Supporting files: `hangman_art.py`, `word_list.py`, `clear_module.py` (for visuals, word data, and clearing screen)
