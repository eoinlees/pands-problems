#Eoin Lees
# This program inputs a positive integer and outputs the value of it if
# value even divide by two
# value odd mulitply it by three and add one
# program ends when current value is 1

# Get positive value from input
x = int(input("Please enter a positive integer: "))

# Return  
if x <= 0:
    print("Please enter a positive number.")
# Use while loop to ensure value is positive and greater than 1. Ends once value is 1. 
while x > 1:   
    if x % 2 == 0: # Divides value by 2 if even
        x = (x/2)
    else:  # multiplies by 3 and adds 1 if off
        x = ((x * 3)+1)
    print(x) # Prints value of input following calculation. restarts loop until x = 1