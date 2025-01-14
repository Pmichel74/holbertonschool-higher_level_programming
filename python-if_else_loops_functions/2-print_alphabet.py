#!/usr/bin/python3

# Ce programme imprime l'alphabet ASCII en minuscules sans nouvelle ligne
# La fonction chr() convertit un code ASCII en caractère
# range(97, 123) génère les codes ASCII de 'a' à 'z'
# end="" empêche l'ajout d'une nouvelle ligne à la fin de chaque print

for i in range(97, 123):
    print("{:c}".format((i)), end="")
