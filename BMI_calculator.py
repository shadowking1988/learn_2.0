print("Welcome to BMI calculator")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight")
else:
    print("You are overweight")
