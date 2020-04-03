# Eoin Lees
# This program outputs whether today is a weekday or not. 
# It runs dependant on the day of the week

# Import datetime module to python
import datetime

# Create tuple to assign days of week in words. 
L = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

# Get day from imported module
today = datetime.datetime.today().weekday()

# Assign name to day number imported
dayName = L[today]
print("Today is {}".format(dayName))

# If statement to print depending of if weekend or not
if today < 5:
    print("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")