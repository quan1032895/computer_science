#-----------------------------------------------------------------------------
# Name:       Set Operations
# Purpose:    Combine and compare sets using set operations.
#
# Author:      Quan
# Created:     4-Apr-2025
# Updated:     8-Apr-2025
#-----------------------------------------------------------------------------
# Create two sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Combine set1 and set2 using the union method
# Union will return all unique numbers from both sets
set3 = set.union(set2, set1)
# Print the union of both sets (all unique numbers from set1 and set2)
print("All the numbers", set3)
# Find the intersection of set1 and set2 using the intersection method
# Intersection will return the numbers that are common to both sets
set4 = set.intersection(set2, set1)
# Print the common numbers between set1 and set2
print("Common numbers", set4)
# Find the difference between set2 and set1 using the difference method
# Difference will return the numbers in set2 but not in set1
set5 = set.difference(set2, set1)
# Print the numbers that are in set2 but not in set1
print("Difference numbers", set5)
