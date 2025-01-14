# This program prints the ASCII alphabet in lowercase without a new line.
print("".join("{}".format(chr(i)) for i in range(97, 123)), end="")
