#-----------------------------------------------------------------------------
# Name:       Countdown timer
# Purpose:    Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.
#
# Author:      Quan
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
num = 10  # Initialize the countdown starting at 10

while num > 0:  # Loop as long as `num` is greater than 0
    print(num)  # Display the current countdown number
    num -= 1  # Decrease `num` by 1 to count down


    user = input("Enter stop to cancel or press Enter:")  # Prompt the user for input
    if user == "stop":  # If the user enters "stop"
        print("Countdown stopped!")  # Acknowledge the stop
        break  # Exit the loop immediately

if num == 0:  # If the countdown completed normally
    print("Countdown completed!")  # Notify the completion
