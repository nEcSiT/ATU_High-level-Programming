# Writing the 2 to 30 times tables

def ranges(number1, number2):
    while number1 < number2:
      number1 = number1 + 1
      return number1

print("Writting the 2 to 20 times table")

for counting in ranges(1, 5):

    print(f"Times table of {counting}")
    for number in ranges(1,13):
        print(f"{counting} x {number} = {counting * number}")

    print("-" * 20)


'''print("Writting the 2 to 8 times table")
count  = 2
while count <= 8:
    print(f"Printing the {count} times table")
    number = 1
    while number <= 12:
        print(f"{count} x {number} = {count*number}")
        number = number + 1
    print("_" * 15)
    count = count + 1
    '''







  
