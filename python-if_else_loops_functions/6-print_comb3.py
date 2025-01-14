#!/usr/bin/python3

# Boucle pour le premier chiffre de 0 à 9
for i in range(10):
    # Boucle pour le deuxième chiffre de i+1 à 9
    for j in range(i + 1, 10):
        # Vérifie si c'est la dernière combinaison (8 et 9)
        if i == 8 and j == 9:
            # Imprime "89" sans virgule après
            print("{:d}{:d}".format(i, j))
        else:
            # Imprime la combinaison suivie de ", "
            print("{:d}{:d}".format(i, j), end=", ")
            