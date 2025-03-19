#-----------------------------------------------------------------------------
# Name:       Guess the number
# Purpose:    generates a random number and keep asking until the user get it right.
#
# Author:      Quan
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------

import random
random.randint(1, 10)
while True:
    num = int(input("Guess a number between 1 and 10: "))
    if num == random.randint(1, 10):
        print("🤣🤣🤣🤣🤣🤣")
        print("Good boy")
        exit()
    else:
        print()

