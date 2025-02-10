#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]

    # Pour chaque ligne restante (n-1 car on a déjà la première)
    for i in range(n - 1):
        # Obtenir la dernière ligne du triangle
        current_row = triangle[-1]
        # Commencer la nouvelle ligne avec 1
        new_row = [1]

        # Pour chaque paire d'éléments dans la ligne courante
        for j in range(len(current_row) - 1):
            # Ajouter la somme des deux nombres au-dessus
            sum = current_row[j] + current_row[j + 1]
            new_row.append(sum)

        # Terminer la ligne avec 1
        new_row.append(1)
        # Ajouter la nouvelle ligne au triangle
        triangle.append(new_row)

    return triangle
