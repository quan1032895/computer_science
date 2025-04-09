#-----------------------------------------------------------------------------
# Name:       Unique Words in a Sentence
# Purpose:    Extract unique words from a sentence using a set.
#
# Author:      Quan
# Created:     04-Apr-2025
# Updated:     09-Apr-2025
#-----------------------------------------------------------------------------
# Given sentence
sentence = "The quick brown fox jumps over the lazy dog"
# Split the sentence into words
words = sentence.split()
# Convert the list of words into a set to get unique words
unique_words = set(words)
# Print the set of unique words
print(unique_words)


