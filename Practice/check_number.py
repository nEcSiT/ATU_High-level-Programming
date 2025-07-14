"""
A program to check if a number is even or odd or zero
"""

number = int(input("Enter a number: "))

if (number % 2 == 0 and number != 0):
    print(f"{number} is even")
elif (number % 2 == 1):
    print(f"{number} is odd")
else:
    print(f"{number} is zero")