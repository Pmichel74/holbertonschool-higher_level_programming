#!/usr/bin/python3

def print_last_digit(number):
    # Get the last digit using modulo and abs() for negative numbers
    last_digit = abs(number) % 10

    # Print the last digit without newline and return it
    print("{}".format(last_digit), end="")
    return last_digit
