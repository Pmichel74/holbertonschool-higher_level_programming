#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add

# Define variables a and b
a = 1
b = 2

# Main execution block
if __name__ == "__main__":
    # Calculate the result of add(a, b)
    result = add(a, b)
    # Print the result in the required format
    print("{} + {} = {}".format(a, b, result))
