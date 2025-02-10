#!/usr/bin/python3
"""Defines a file-writing and file-appending functions."""


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
    # Écrit texte fichier et retourne nbr de caractères écrits
        return f.write(text)


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
        # Ajoute le texte à la fin du fichier et retourne le nombre de caractères ajoutés
        return f.write(text)
