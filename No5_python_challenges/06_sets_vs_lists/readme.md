
# Challenge 7: Sets vs Lists  

### Concept  
Understanding the key differences between **sets** and **lists** in Python.

###  Objective  
Compare how sets and lists behave, especially regarding duplicates.

###  Task  
- Create a list: `num_list = [1, 2, 2, 3, 4, 4, 5]`  
- Convert it into a set  
- Print both the list and the set  

###  Code Example
```python
# Create a list of numbers with duplicate values
num_list = [1, 2, 2, 3, 4, 4, 5]

# Print the original list (includes duplicates)
print("List:", num_list)

# Convert the list into a set to remove duplicates
num_set = set(num_list)

# Print the set (shows only unique numbers)
print("Set:", num_set)


