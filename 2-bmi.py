# Eoin Lees
# This program calculates a persons Body Mass Index.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))

#weight = 65
#height = 180

#convert Height to meters

hm = height / 100

#square height

hsqr = (hm * hm)

bmi = round(weight/hsqr,2)

print("Your bmi is:", bmi)

#Notes: review lecture 1 for basics on variables / inputs etc.. 
# Add in bmi definitions? If over then etc...

