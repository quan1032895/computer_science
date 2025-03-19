#-----------------------------------------------------------------------------
# Name:        Eligible voting system
# Purpose:     Check if the person is eligible to vote based on their age
#
# Author:      Quan
# Created:     27-Feb-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Welcome to the age checking system!")
age = int(input("How old are you? "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote.")