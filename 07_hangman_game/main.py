import hangman_art
import random
import word_list
from clear_module import clear
Stages = hangman_art.stages

Logo = hangman_art.logo
print(Logo)
words_list = word_list.word_list
chosen_word = random.choice(words_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    clear()
   
    if guess in display:
      print("You've already guessed that letter.")
   
    for position in range(word_length):
      letter = chosen_word[position]
       
      if letter == guess:
        display[position] = letter

    
    if guess not in chosen_word:
        print("Oops! That letter is not in the word.")
       
        lives -= 1
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(Stages[lives])
