# Hangman Game
# This program implements a simple text-based Hangman game. 
# The user is prompted to guess letters in a randomly chosen word 
# from a predefined list. The game continues until the user 
# either guesses the word correctly or runs out of attempts. 
# The current status of the word and the number of remaining guesses 
# are displayed to the user after each guess.
#
# Author: iamraffa
# Date: 29/10/2024

import words
import random

chosen_word = random.choice(words.words)
word_letters = list(chosen_word)
current_word = []
remaining_guesses = 10

for _ in range(0, len(chosen_word)):
    current_word.append(".")

while (word_letters != current_word) and (remaining_guesses > 0):
    print("------------------------------------------------------------")
    print(" HANGMAN - Current word status:", " ".join(current_word))
    print("------------------------------------------------------------")

    print(f"\n You have {remaining_guesses} guesses remaining.")
    guessed_letter = input(" Guess a letter: ").lower()

    if guessed_letter not in current_word:
        if guessed_letter in chosen_word:
            for index, letter in enumerate(word_letters):
                if letter == guessed_letter:
                    current_word[index] = letter
            print(f"\n Great! The letter '{guessed_letter}' is in the word.\n")
        else:
            remaining_guesses -= 1
            print(f"\n The letter '{guessed_letter}' is not in the word. You lost one attempt.")
            print(f" Remaining guesses: {remaining_guesses}\n")
    else:
        print(f"\n You have already chosen the letter '{guessed_letter}'.\n")

if current_word == word_letters:
    print(" Congratulations! You guessed the word:", chosen_word)
else:
    print(" You ran out of attempts. The word was:", chosen_word)
