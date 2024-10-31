# Caesar Cipher Program
# This program implements a simple text-based Caesar cipher 
# encryption and decryption tool. The user can choose to 
# either encrypt or decrypt a message by specifying a shift 
# value. The program continues to prompt the user for messages 
# and operations until they choose to exit. The transformed 
# message is displayed to the user after each operation.
#
# Author: iamraffa
# Date: 31/10/2024

import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    new_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_text += alphabet[index]
        else:
            new_text += letter

    print(f"\nYour new word is '{new_text}'")

print(art.logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    if input("\nDo you want to continue? (yes/no): ").lower() == 'no':
        should_continue = False
        print("\nGoodbye! See you next time!")
    else:
        print("\n")
