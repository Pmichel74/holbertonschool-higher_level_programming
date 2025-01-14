#!/usr/bin/python3

# This program prints the ASCII alphabet in lowercase without 'q' and 'e', without a new line.
print("".join("{}".format(chr(i)) for i in range(97, 123) if chr(i) not in ['q', 'e']), end="")
