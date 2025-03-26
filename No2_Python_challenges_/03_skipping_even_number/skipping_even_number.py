#-----------------------------------------------------------------------------
# Name:       Skip the even number
# Purpose:    Write a program that prints numbers from `1` to `10`, but **skips even numbers** using the `continue` statement.
#
# Author:      Quan
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
for i in range(1, 11):  # Loop through numbers from 1 to 10
    if i % 2 == 0:  # Check if the number is even
        continue  # Skip the rest of the loop for even numbers
    print(i)  # Print the number if it is odd





#easier way
# for i in range (1, 10, +2):
#print(i)