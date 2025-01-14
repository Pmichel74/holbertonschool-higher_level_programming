#!/usr/bin/python3
# This program generates a random number and prints the last digit of that number with a message.
import random
number = random.randint(-10000, 10000)

# Obtenir le dernier chiffre du nombre
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Construire et imprimer le message approprié
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
