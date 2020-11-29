uHeight = float(input("What is your height in inches?"))
uWeight = float(input("What is your weight in pounds?"))
BMI = uWeight / (uHeight**2) * 703

print("Your BMI is ",format(BMI,'.2f'))
