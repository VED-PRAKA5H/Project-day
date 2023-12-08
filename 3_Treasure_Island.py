#from "ascii.co.uk/art" we take below ascii art
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____$______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
print("Welcome to treasure Island!")
choice1=input('you\'re at $ symbol, where do you want to go? Type "left" or "right".\n').lower()
if choice1=="left":
  choice2 = input('you\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat OR type "swim" to swim across\n').lower()
  if choice2 == "wait":
    choice3 = input("You have arrived at the island unharmed. There is a house with doors of dstinct colours red, blue and yellow which colour will you choose?\n")
    if choice3 == "red":
      print("It's a room full of fire. GAME OVER!")
      
    elif choice3 == "yellow":
      print("You found the treasure : YOU WIN!")
    
    elif choice3 == "blue":
      print("You drown in the water well. GAME OVER!") 
      
    else :
      print("You enter a room full of beasts. GAME OVER!")
     
  else:
    print("Yougot attacked by an angry trouts. GAME OVER!")

else:
  print("You fell in a hole. GAME OVER!")
