#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    # Ouvre le fichier en mode lecture avec encodage UTF-8
    with open(filename, encoding="utf-8") as f:
        # Lit le contenu du fichier et l'affiche sur stdout
        print(f.read(), end="")
