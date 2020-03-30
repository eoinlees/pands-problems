# Eoin Lees
# This program displayes a plot of the function:
# f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0,4]
# on the one set of axes

# Import numpy and matplotlib to python
import numpy as np
import matplotlib.pyplot as plt

# Define Functions
def f(x):
    return x
def g(x):
    return x**2
def h(x):
    return x**3

#Define x in the range (0,4) using numpy linespace 
# number of divisions in range set at 50
x = np.linspace(0.0,4.0,50)

#Plot the  x value vs the function of x

plt.plot(x, f(x), "b.", label="f(x)=x")
plt.plot(x, g(x), "r.", label="g(x)=x^2")
plt.plot(x, h(x), "g.", label="h(x)=x^3")

#Label and title the plot
plt.title("Weekly Task 8")
plt.legend()
plt.xlabel("x in the range (0,4)")
plt.ylabel("function of x in the range (0,4)")

#Show plot after running command on python
plt.show()