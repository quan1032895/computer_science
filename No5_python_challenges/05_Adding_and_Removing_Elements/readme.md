# Challenge 6: Adding and Removing Elements (Using `update()` and `discard()`)

## Concept  
Use `.update()` to add multiple elements to a set, and `.discard()` to safely remove an item without errors.

## Objective  
Modify a set efficiently by adding and removing elements.

## Task  
- Create a set: `letters = {'a', 'b', 'c'}`
- Add multiple elements: `'d'`, `'e'`, `'f'` using `.update()`
- Remove `'b'` using `.discard()`
- Convert the set to a list and sort it
- Print the sorted list

## Code Example
```python
# Create the original set
letters = {'a', 'b', 'c'}

# Add multiple elements to the set
letters.update(['d', 'e', 'f'])

# Remove the element 'b' if it exists
letters.discard('b')

# Sort the set by converting it into a list
sorted_letters = sorted(letters)

# Print the sorted list of letters
print(sorted_letters)


