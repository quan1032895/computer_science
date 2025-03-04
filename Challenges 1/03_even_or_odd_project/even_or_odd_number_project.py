#-----------------------------------------------------------------------------
# Name:        Odd or Even checking system
# Purpose:     Check what is the number the user entered is odd or even
#
# Author:      Quan
# Created:     26-Feb-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Even or Odd Number Checking System ")
num = int(input("Please enter a number: "))
if num  % 2 == 0:
    print("You entered", num)
    print("This is an even number")
elif num  % 2 !=0 :
    print("You entered", num)
    print("This is an odd number")
else:
    print("Invalid Number")

