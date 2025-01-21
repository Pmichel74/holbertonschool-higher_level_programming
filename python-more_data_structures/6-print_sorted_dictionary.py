#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    # sorted() retourne une nouvelle liste des clés triées
    # Parcourt chaque clé dans l'ordre alphabétique
    for k in sorted(a_dictionary):
        # Affiche "clé: valeur" pour chaque élément
        print("{}: {}".format(k, a_dictionary[k]))
