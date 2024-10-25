# Tip Calculator
# This program calculates the amount each person needs to pay when splitting a bill,
# including a customizable tip percentage. It prompts the user for the total bill amount,
# the desired tip percentage (10%, 12%, or 15%), and the number of people sharing the bill.
# The final output is the amount each person should contribute.
#
# Author: iamraffa
# Date: 25/10/2024

print("Welcome to the tip calculator!")
total_bill = float(input("What's the total bill?  $ "))
tip = float(input("How much tip do you wanna give? "))
number_people = int(input("How many people are splitting the bill? "))

price_per_person = round((total_bill + ((tip / 100) * total_bill)) / number_people, 2)

print(f"Each person should pay: ${price_per_person}")