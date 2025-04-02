# Create a tuple containing a list of fruits  
SET fruits TO ("apple", "banana", "apple", "cherry", "orange", "apple")  
# Print a message introducing the list of fruits  
PRINT "This is the list of the fruits"  
# Print the tuple containing the fruits  
PRINT fruits  
# Ask the user to enter the name of a fruit  
DISPLAY "Enter the fruit name: "  
SET user_ask TO INPUT()  
# Count how many times the entered fruit appears in the tuple  
SET count TO COUNT(user_ask IN fruits)  
# Print the count of the entered fruit  
PRINT count  
