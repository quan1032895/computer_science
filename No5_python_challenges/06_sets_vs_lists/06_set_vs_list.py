#-----------------------------------------------------------------------------
# Name:       Sets vs Lists
# Purpose:    Compare the behavior of sets and lists.
#
# Author:      Quan
# Created:     04-Apr-2025
# Updated:     09-Apr-2025
#-----------------------------------------------------------------------------
# Create a list of numbers with some duplicates
num_list = [1, 2, 2, 3, 4, 4, 5]
# Print the original list (shows duplicates)
print("List:", num_list)
# Convert the list to a set to remove duplicate values
num_set = set(num_list)
# Print the set (only unique numbers will be shown)
print("Set:", num_set)
