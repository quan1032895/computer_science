#-----------------------------------------------------------------------------
# Name:       Sum of the number
# Purpose:    to calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      Quan
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------
n = int(input("Enter a number: "))  # Prompt the user to enter a number
sum = 0  # Initialize a variable to store the sum
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    sum += i  # Add the current number `i` to the sum
print("Sum =", sum)  # Print the final sum

