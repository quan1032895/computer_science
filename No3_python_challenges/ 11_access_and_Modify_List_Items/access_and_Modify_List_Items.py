#-----------------------------------------------------------------------------
# Name:       Access and Modify List Items
# Purpose:    Modify a grocery list by changing an existing item.
#
# Author:      Quan
# Created:     24-Mar-2025
# Updated:     24-Mar-2025
#-----------------------------------------------------------------------------
grocery_list = ["apple", "banana", "carrots", "milk", "bread"]  # Initialize list
grocery_list.insert(2, "grapes")  # Insert "grapes" at index 2
grocery_list.remove("banana")  # Remove "banana" from the list
print(grocery_list)  # Print the list
print(grocery_list[2])  # Print item at index 2 ("carrots")