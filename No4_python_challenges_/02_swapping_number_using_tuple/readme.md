# Take the first number as input from the user and convert it to an integer  
SET num1 TO INPUT("Enter a first number: ") AS INTEGER  
# Take the second number as input from the user and convert it to an integer  
SET num2 TO INPUT("Enter a second number: ") AS INTEGER  
# Store both numbers in a list  
SET list1 TO [num1, num2]  
# Print the original list before swapping  
PRINT list1  
# Display a message indicating that the numbers will be swapped  
PRINT "Swapping the number"  
# Swap the number by printing the index in the opposite way
PRINT list1[1], list1[0]

