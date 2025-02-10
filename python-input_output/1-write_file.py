#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    # Ouvre le fichier en mode écriture avec encodage UTF-8
    # Si le fichier n'existe pas, il sera créé
    with open(filename, "w", encoding="utf-8") as f:
        # Écrit texte fichier et retourne le nombre de caractères écrits
        return f.write(text)
