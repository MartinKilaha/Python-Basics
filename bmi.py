weight = float(input("Enter your weight in kilograms"))
height = float(input("Enter your height in meters"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
print(f"Your BMI is {bmi:.2f} and your classification is : {category}")
