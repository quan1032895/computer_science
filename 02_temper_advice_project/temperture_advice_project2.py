#-----------------------------------------------------------------------------
# Name:        Temperature advice system
# Purpose:     Give the user the advice of what to wear based on the temperature
#
# Author:      Quan
# Created:     25-Feb-2025
# Updated:     3-Mar-2025
#-----------------------------------------------------------------------------
print("Welcome to the weather adviser!")
tem = int(input("What is the temperature today(in Celsius)?:"))
if tem < 10:
    print("Today the weather is", tem,"°C")
    print("It's cold outside. Wear a jacket!")
elif tem >= 10 and tem <= 25:
    print("Today the weather is", tem,"°C")
    print("It's a nice day. Wear short sleeves!")
elif tem > 25:
    print("Today the weather is", tem, "°C")
    print("It's hot outside. Stay cool")
else:
    print("Today the weather is", tem, "°C")
    print("Ooh the weather look tough you should stay inside, it is not good for your health")
print("Thank you for using our service")
print("Have a nice day!")