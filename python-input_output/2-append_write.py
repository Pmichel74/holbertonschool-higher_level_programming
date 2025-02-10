#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    # Ouvre le fichier en mode ajout avec encodage UTF-8
    # Si le fichier n'existe pas, il sera créé
    with open(filename, "a", encoding="utf-8") as f:
        # Ajoute txt à la fin du fichier et retourne nbre de caract ajoutés
        return f.write(text)
