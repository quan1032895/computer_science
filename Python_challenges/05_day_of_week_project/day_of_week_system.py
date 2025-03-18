#-----------------------------------------------------------------------------
# Name:        Day of the week project
# Purpose:     The system suggests an activity based on the day of the week
#
# Author:      Quan
# Created:     28-Feb-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Hello")
day = input("What day of the week is it?")
if day == "Monday" or "monday":
    print("Start your week with a workout")
elif day == "Tuesday" or "tuesday":
    print("It's a great day to read a book")
elif day == "Wednesday" or "wednesday":
    print("Mid-week movie night!")
elif day == "Thursday" or "thursday":
    print("Try a new recipe")
elif day == "Friday" or "friday":
    print("Relax and enjoy the weekend!")
elif day == "Saturday" or "saturday":
    print("Go for a hike")
elif day == "Sunday" or "sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("Please enterd the day of the week correctly.")
