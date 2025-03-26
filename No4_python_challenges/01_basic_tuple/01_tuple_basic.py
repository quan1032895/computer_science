#-----------------------------------------------------------------------------
# Name:       Tuple Basic
# Purpose:    Create a tuple with five different elements, including an integer, a float, a string, a boolean, and another tuple
#
# Author:      Quan
# Created:     28-Mar-2025
# Updated:     01-Apr-2025
#-----------------------------------------------------------------------------
# Defining a tuple with different data types: integer, float, string, boolean, and another tuple
tuple = (42, 3.14, 'Python', True, (1, 2, 3))
# Printing the entire tuple
print(tuple)
# Accessing and printing the third element (index 2) of the tuple, which is a string: 'Python'
print(tuple[2])
# Accessing the first element (index 0) of the nested tuple (index 4 in the main tuple)
print(tuple[4][0])  # Output

