weight, hieght = int(input("Please enter your weight: ")), float(input("Please enter your heingt: "))


bmi = round(weight / (hieght ** 2), 2)
#print(f"Your BMI is: {bmi: .2f}")

if (bmi < 16.0):
    print(f"Your BMI is {bmi}, meaning you are severely thin")

elif (16.0 < bmi < 16.9):
    print(f"You BMI is {bmi}, means you are moderately thin")

elif (17.0 <= bmi <= 18.4):
    print(f"You BMI is {bmi}, means you are mildely thin")

elif (18.5 <= bmi <= 24.4):
    print(f"You BMI is {bmi}, means you are in the normal range")

elif (25.0 <= bmi <= 29.9):
    print(f"You BMI is {bmi}, means you are overweight [Pre-obese]")

elif (30.0 <= bmi <= 34.9):
    print(f"You BMI is {bmi}, means you are obese (Class I)")

elif (35.0 <= bmi <= 39.9):
    print(f"You BMI is {bmi}, means you are obese (Class II)")

else:
    print(f"You BMI is {bmi}, means you are Obese (Class III)")