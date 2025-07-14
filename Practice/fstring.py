"""
name = "Nicholas"
age = 20
height = 2.5

print(f"My name is {name} and I am {age} years old, my height is {height} ft")

"""

age = int(input("Enter your age: "))
years_left = 90 - age

months = years_left * 12
weeks = years_left * months
days = years_left * weeks

print(f"You have {months} months, {weeks} weeks and {days} days")
