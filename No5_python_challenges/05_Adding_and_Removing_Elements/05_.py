#-----------------------------------------------------------------------------
# Name:       Adding and Removing Elements (Using Update and Discard)
# Purpose:    Demonstrate various set methods
#
# Author:      Quan
# Created:     04-Apr-2025
# Updated:     09-Apr-2025
#-----------------------------------------------------------------------------
# Create the original set
letters = {'a', 'b', 'c'}
# Add multiple elements
letters.update(['d', 'e', 'f'])
# Remove 'b'
letters.discard('b')
# Sort the set by converting it to a list
sorted_letters = sorted(letters)
# Print the sorted result
print(sorted_letters)



