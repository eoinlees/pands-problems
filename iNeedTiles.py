# Program to calculate the amount of tiles needed for bathroom
# In meters squared


length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width

needed = area * 1.05

print("you need ",needed,"tiles in meters squared.")