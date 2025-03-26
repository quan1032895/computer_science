#-----------------------------------------------------------------------------
# Name:       Sorting and Reversing a List
# Purpose:    Work with sorting and reversing lists
#
# Author:      Quan
# Created:     25-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------
# Create a tuple containing a list of fruits (including duplicate values)
fruits = ("apple", "banana", "apple", "cherry", "orange", "apple")
# Print a message introducing the list of fruits
print("This is the list of the fruits")
# Print the tuple containing the fruits
print(fruits)
# Ask the user to enter the name of a fruit
user_ask = input("Enter the fruit name: ")
# Count how many times the entered fruit appears in the tuple
count = fruits.count(user_ask)
# Print the count of the entered fruit in the tuple
print(count)
