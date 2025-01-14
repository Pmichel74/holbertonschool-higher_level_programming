#!/usr/bin/python3

# Define the function uppercase
def uppercase(str):
    # Iterate over each character in the string
    for i in str:
        # Check if the character is lowercase (ASCII range 97 to 122)
        if ord(i) >= 97 and ord(i) <= 122:
            # Convert lowercase character to uppercase
            # by subtracting 32 from its ASCII value
            i = chr(ord(i) - 32)
        # Print the character without a newline at the end
        print("{}".format(i), end="")
    # Print a newline after the loop completes
    print()
