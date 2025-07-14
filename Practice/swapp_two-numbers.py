number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
# Swap the numbers
temp = number_1
number_1 = number_2
number_2 = temp
print(f"First number: {number_1}")
print(f"Second number: {number_2}")
# Swap the numbers without using a third variable
add_number = number_1 + number_2
print(f"The sum of {number_1} and {number_2} is {add_number}")