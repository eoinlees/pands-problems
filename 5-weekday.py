# Eoin Lees
# This program outputs whether today is a weekday or not. 
# It runs dependant on the day of the week

import datetime
import calendar

L = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

today = datetime.datetime.today().weekday()

dayName = L[today]
print("Today is {}".format(dayName))

if today < 5:
    print("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")

#Note: Test on weekend - ensure program works each day. 