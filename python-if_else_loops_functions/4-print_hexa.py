#!/usr/bin/python3

# Prints all numbers from 0 to 98 in decimal and in hexadecimal
print("\n".join("{} = 0x{:x}".format(i, i) for i in range(99)))
