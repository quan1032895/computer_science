#-----------------------------------------------------------------------------
# Name:       Student grading system
# Purpose:    To grade the student based on the mark they got
#
# Author:      Quan
# Created:     24-Feb-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Welcome to the Student Grading System")
grade = int(input("Enter your Grade for this sem: "))
if grade >= 90:
    print("grade A")
elif grade >= 80 and grade <= 89:
    print("grade B")
elif grade >= 70 and grade <= 79:
    print("grade C")
elif grade >= 60 and grade <= 69:
    print("grade D")
elif grade < 60:
    print("grade F")
else:
    print("Invalid Grade")
