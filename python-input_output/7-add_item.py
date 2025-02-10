#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    # Importer les fonctions save_to_json_file et load_from_json_file
    save_to_json_file = (
        __import__('5-save_to_json_file').save_to_json_file
    )
    load_from_json_file = (
        __import__('6-load_from_json_file').load_from_json_file
    )

    try:
        # Charger la liste existante à partir du fichier add_item.json
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # Si le fichier n'existe pas, initialiser une liste vide
        items = []

    # Ajouter les arguments de la ligne de commande à la liste
    items.extend(sys.argv[1:])

    # Sauvegarder la liste mise à jour dans le fichier add_item.json
    save_to_json_file(items, "add_item.json")
