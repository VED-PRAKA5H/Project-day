import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
print("Welcome Rock Paper Scissors Game!")
player_choice = int(input("What do you choose? Type 0 for Rock ,1 for Scissors and 2 for Paper\n"))

computer_choice = random.randint(0, 2)

if player_choice == computer_choice:
    if player_choice == 0:
        print(f"you chose:\n{rock}\ncomputer chose:\n{rock}\nGAME TIED!")
    if player_choice == 1:
        print(f"you chose:\n{paper}\ncomputer chose:\n{paper}\nGAME TIED!")
    if player_choice == 1:
        print(f"you chose:\n{scissors}\ncomputer chose:\n{scissors}\nGAME TIED!")


elif player_choice != computer_choice:
    if player_choice == 0 and computer_choice == 1:
        print(f"you chose:\n{rock}\ncomputer chose:\n{scissors}\nYOU WIN!")
    if player_choice == 0 and computer_choice == 2:
        print(f"you chose:\n{rock}\ncomputer chose:\n{paper}\nYOU WIN!")
    if player_choice == 1 and computer_choice == 0:
        print(f"you chose:\n{scissors}\ncomputer chose:\n{rock}\nYOU LOST!")
    if player_choice == 1 and computer_choice == 2:
        print(f"you chose:\n{scissors}\ncomputer chose:\n{paper}\nYOU WIN!")
    if player_choice == 2 and computer_choice == 0:
        print(f"you chose:\n{paper}\ncomputer chose:\n{rock}\nYOU LOST!")
    if player_choice == 2 and computer_choice == 1:
        print(f"you chose:\n{paper}\ncomputer chose:\n{scissors}\nLOST!")

if player_choice > 2 or player_choice < 0:
    print("You entered wrong input. YOU LOST!")

    # BY USING LIST 👇

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# computer_choice = random.randint(0, 2)


# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 

# else:
#   print("You chose:\n"+game_images[user_choice])
#   print("Computer chose:")
#   print(game_images[computer_choice])

#   if user_choice == 0 and computer_choice == 2:
#     print("You win!")
#   elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#   elif computer_choice > user_choice:
#     print("You lose")
#   elif user_choice > computer_choice:
#     print("You win!")
#   elif computer_choice == user_choice:
#     print("It's a draw")
