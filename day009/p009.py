# Secret Auction Program
# This program implements a simple text-based auction system 
# where users can place bids. Each bidder enters their name 
# and bid amount, and the program collects bids until there 
# are no more bidders. The highest bid is then determined, 
# and the winner is announced. The program provides a clean 
# interface for multiple bidders to participate in the auction.
#
# Author: iamraffa
# Date: 31/10/2024

import art
import os

bid_dictionary = {}
should_collect = True

def define_winner(bid_dictionary):
    winner_name = ""
    winner_bid = 0

    for bidder in bid_dictionary:
        if int(bid_dictionary[bidder]) > winner_bid:
            winner_bid = int(bid_dictionary[bidder])
            winner_name = bidder

    print(art.logo)
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print(art.logo)
print("Welcome to the secret auction program.")

while should_collect:
    name = input("What is your name? ")
    bid = input("What is your bid? $ ")
    bid_dictionary[name] = bid

    more_bidders = input("Are there any other bidders? (yes/no) ").lower()
    if more_bidders == "no":
        should_collect = False

    clear_screen()

define_winner(bid_dictionary)
