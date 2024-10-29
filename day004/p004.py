# Rock, Paper, Scissors Game
# This program allows the user to play a game of Rock, Paper, Scissors against the computer.
# The user is prompted to choose Rock (0), Paper (1), or Scissors (2). The computer makes a 
# random choice, and the program determines the winner based on the rules of the game. 
# The final output displays both choices and announces the result: win, lose, or draw.
#
# Author: iamraffa
# Date: 27/10/2024

import options
import random

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
core_option = random.randint(0, 2)

if user_option >= 0 and user_option <= 2:
    print("\nYou chose")
    print(options.options[user_option])

    print("Computer chose")
    print(options.options[core_option])

    if user_option == core_option:
        print('You draw')
        
    else:
        if user_option == 0:
            if core_option == 2:
                print("You win, rock wins against scissors")
            else:
                print("You lose, rock loses against paper")

        elif user_option == 1:
            if core_option == 0:
                print("You win, Paper wins against rock")
            else:
                print("You lose, Paper loses against scissors")

        elif user_option == 2:
            if core_option == 1:
                print("You win, Scissors wins against paper")
            else:
                print("You lose, Scissors loses against rock")

else:
    print(f"{user_option} is not a valid option. Please choose 0, 1, or 2.")
