#-----------------------------------------------------------------------------
# Name:       Sum of the number
# Purpose:    to calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      Quan
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =" ,sum)
