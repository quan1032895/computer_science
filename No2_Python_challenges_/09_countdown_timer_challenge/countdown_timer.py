#-----------------------------------------------------------------------------
# Name:       Countdown timer
# Purpose:    Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.
#
# Author:      Quan
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
num = 10
while num >0:
    print(num)
    num -=1
    user = input("Enter stop to cancel or press Enter:")
    if user == "stop":
        print("Countdown stopped!")
        break
if num == 0 :
    print("Countdown completed!")
