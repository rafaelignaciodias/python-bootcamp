# Password Generator
# This program generates a random password based on user-defined criteria. 
# The user is prompted to specify the number of letters, symbols, and numbers 
# they would like in their password. The program randomly selects characters 
# from predefined lists and shuffles them to create a secure password. 
# The final output displays the generated password to the user.
#
# Author: iamraffa
# Date: 28/10/2024

import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [];

if nr_letters > 0:
    for _ in range(0, nr_letters):
        password.append(random.choice(letters_list))

if nr_symbols > 0:
    for _ in range(0, nr_symbols):
        password.append(random.choice(symbols_list))

if nr_numbers > 0:
    for _ in range(0, nr_numbers):
        password.append(random.choice(numbers_list))

random.shuffle(password)

final_password = ''.join(password)
print(f"Your strong password is: {final_password}")
