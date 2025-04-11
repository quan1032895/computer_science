#-----------------------------------------------------------------------------
# Name:       Challenge 2: Swapping Values Using Tuples
# Purpose:    Python allows swapping values easily using tuples.
#
# Author:      Quan
# Created:     29-Mar-2025
# Updated:     01-Apr-2025
#-----------------------------------------------------------------------------
# Display a welcome message for the swapping number system
print("Welcome to the swapping number system")
# Take the first number as input from the user and convert it to an integer
num1 = int(input("Enter a first number: "))
# Take the second number as input from the user and convert it to an integer
num2 = int(input("Enter a second number: "))
# Store both numbers in a list
list1 = [num1, num2]
# Print the original list before swapping
print(list1)
# Display a message indicating that the numbers will be swapped
print("Swapping the number")
# Attempting to print swapped values, but there's an error in using 'list' instead of 'list1'
# 'list' is a reserved keyword in Python and should not be used as a variable name
print(list1[1], list1[0])  # Corrected from 'list' to 'list1'



0
