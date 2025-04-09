# Challenge 2: Unique Words in a Sentence

## Concept  
Extracting unique words from text using sets.

## Objective  
Extract unique words from a sentence using a set.

## Task  
- Given a sentence: `sentence = "The quick brown fox jumps over the lazy dog"`, convert it into a set of unique words.
- Print the set of unique words.

## Code Example
```python
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
unique_words = set(words)
print(unique_words)
