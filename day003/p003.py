# Treasure Island Adventure
# This program takes you on an adventure to find hidden treasure. 
# You will navigate through choices at a crossroads, decide on actions, 
# and face challenges that lead to either victory or defeat. 
# The game prompts the user to choose paths and make decisions 
# that determine the outcome of their quest.
#
# Author: iamraffa
# Date: 26/10/2024

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You're at a crossroads. Where do you want to go?")
side = input('Type "left" or "right": ')

if side.lower() == 'left':
    print("You've chosen the left path. What do you want to do?")
    action = input('Type "swim" or "wait": ')

    if action.lower() == 'swim':
        print("You dive in! Which door do you want to go through?")
        door = input('Type "red", "blue", or "yellow": ')

        if door.lower() == "red":
            print("Oh no! You got burned by fire. Game Over.")
        elif door.lower() == "blue":
            print("Yikes! You were eaten by beasts. Game Over.")
        elif door.lower() == "yellow":
            print("Congratulations! You found the treasure. You Win!")
        else:
            print("That's not a door! Game Over.")

    elif action.lower() == 'wait':
        print("A swarm of angry trout attacks you. Game Over.")

    else:
        print("That's not a valid action. Game Over.")

elif side.lower() == 'right':
    print("Oops! You fell into a hole. Game Over.")

else:
    print("That's not a valid direction. Game Over.")
