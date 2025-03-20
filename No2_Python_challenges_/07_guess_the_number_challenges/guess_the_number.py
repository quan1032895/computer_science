#-----------------------------------------------------------------------------
# Name:       Guess the number
# Purpose:    generates a random number and keep asking until the user get it right.
#
# Author:      Quan
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------

import random  # Import the random module to generate random numbers

random.randint(1, 10)  # Generate a random number between 1 and 10

while True:  # Start an infinite loop to keep asking the user for input
    num = int(input("Guess a number between 1 and 10: "))  # Prompt the user to guess a number
    if num == random.randint(1, 10):  # Check if the guess matches the random number
        print("🤣🤣🤣🤣🤣🤣")  # Print a success message
        print("Good boy")  # Print congratulations
        exit()  # Exit the program if guessed correctly
    else:
        print()  # If wrong, just print an empty line and continue the loop


