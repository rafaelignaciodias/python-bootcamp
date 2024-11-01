# Simple Calculator Program
# This program implements a text-based calculator 
# that performs basic arithmetic operations: addition, 
# subtraction, multiplication, and division. 
# Users can input two numbers and choose an operation, 
# and the program displays the result. The user can 
# continue performing calculations or exit the program 
# at their discretion, ensuring a user-friendly experience.
#
# Author: iamraffa
# Date: 01/11/2024

import art
import os

def calculate(first_number, second_number, operation):
    """Perform a calculation based on the given operation."""

    if operation == "+":
        return first_number + second_number

    elif operation == "-":
        return first_number - second_number

    elif operation == "*":
        return first_number * second_number

    elif operation == "/":
        return first_number / second_number

    else:
        return False


def clear_screen():
    """Clear the console screen."""

    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """Main function to run the calculator."""

    clear_screen()
    print(art.logo)

    should_continue = True

    while should_continue:
        p1_number = float(input("What's the first number? "))
        type_operation = input("\nPick an operation ( + - * / ): ")
        p2_number = float(input("\nWhat's the second number? "))

        result = calculate(p1_number, p2_number, type_operation)

        if result is False:
            print("Error: Invalid operation.")
        else:
            print(f"\nResult: {result}")

        choice = input("\nShould we continue? (y/n) ")

        if choice.lower() != "y":
            should_continue = False
        else:
            clear_screen()
            print(art.logo)


if __name__ == "__main__":
    main()
