# Eoin Lees
# This program reads in a text file and outputs 
# the number of e's it contains. 
# It reads the file name from the command line argument.

# Get document from argument
import sys
with open(sys.argv[1],"r") as file: # Open the file in read mode
    data = file.read() # Read the file

# Use count function to count substring "e"
numE = data.count("e")

# Site referenced for data import https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python
# Sites referenced for count https://www.geeksforgeeks.org/python-string-count/

# Print number of e's to 
print(numE)

# Complete for now. Return to enter if statement 
# reguarding no text file added to python command