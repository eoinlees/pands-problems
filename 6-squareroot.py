# Eoin Lees
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root
# by creating a function 

# Get float input for square root calculation
num = float(input("Please enter a positive number: "))

# Define function
def newtonSqr(number, numberIterations = 300):
    a = float(number)
    for _ in range(numberIterations): #Using "_" to declare unused variable
        number = 0.5 * (number + (a/number))
    return number

# Followed example uses here : https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

ans = newtonSqr(num)
# Ensure Positive number
if num <= 0:   
    print("You must enter a positive number for the program to run")
# Print result if positive
else:
    print("The square root of {} is approx. {}".format(num,ans))