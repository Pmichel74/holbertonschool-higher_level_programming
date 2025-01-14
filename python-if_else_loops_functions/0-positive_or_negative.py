#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Vérifiez si le nombre est positif, négatif ou zéro et imprimez le résultat
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

