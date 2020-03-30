# Eoin Lees
# This program reads in a text file and outputs 
# the number of e's it contains. 
# It reads the file name from the command line argument.

# Import sys module
import sys

# Use try command from Topic 9 lectures
try:
    with open(sys.argv[1],"r") as file: # Open the file in read mode
        data = file.read() # Read the file
        numE = data.count("e") # Use count function to count substring "e"
        print("There are {} letter e's in this document.".format(numE)) # Print number of e's 

# Add except block to pick up any errors
except FileNotFoundError: # Except block for incorrect file
    print("The file " + sys.argv[1] + " does not exist in the current folder.")
except IndexError: # Except block for file not in command
    print("Please enter a .txt file in the command.")

# Site referenced for data import https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python
# Sites referenced for count https://www.geeksforgeeks.org/python-string-count/