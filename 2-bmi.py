# Eoin Lees
# This program calculates a persons Body Mass Index.

# Get the inputs from the user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))

# Convert Height to meters
hm = height / 100

# Square height
hsqr = (hm * hm)

# Calculate bmi
bmi = round(weight/hsqr,2)

# Print result
print("Your bmi is:", bmi)

# Extra if statement using WHO bmi classifications
if bmi < 18.50:
    print("According to the WHO You are Underweight.")
elif 18.50 < bmi < 24.99:
    print("According to the WHO You are normal weight.")
elif 25 < bmi < 29.99:
    print("According to the WHO You are overweight.")
else:
    print("According to the WHO You are obese.")