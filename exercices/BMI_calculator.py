height = float(input("Enter your height (in inches): "))
weight = float(input("Enter your weight (in lbs): "))
bmi = round(weight* 703 / height ** 2, 2)

if bmi < 16:
    category = "Severly Underweight!"
elif bmi > 16 and bmi < 18.4:
    category = "Underweight!"
elif bmi > 18.5  and bmi < 24.9:
    category = "Normal"
elif bmi > 25.0 and bmi < 29.9:
    category = "Overweight"
elif bmi > 30.0 and bmi < 34.9:
    category = "Moderately Obese"
elif bmi > 35.0 and bmi < 39.9:
    category = "Severly Obese"
else:
    category = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {category}")