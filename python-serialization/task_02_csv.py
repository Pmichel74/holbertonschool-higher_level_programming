#!/usr/bin/python3
"""Defines function that converts csv to json"""
# Import des modules nécessaires pour CSV et JSON
import csv
import json


def convert_csv_to_json(csv_file):
    """Function writes data to data.json.

    Args:
        csv_file: csv file to convert
        data.json: json file to write to
    """
    # Liste pour stocker toutes les lignes du CSV
    data = []
    try:
        # Ouverture du fichier CSV en mode lecture avec encodage UTF-8
        with open(csv_file, encoding="utf-8") as csvf:
            # Création d'un lecteur de dictionnaire CSV
            readcsv = csv.DictReader(csvf)
            # Parcours de chaque ligne du CSV
            for row in readcsv:
                # Ajout de la ligne (dictionnaire) à la liste
                data.append(row)
    except FileNotFoundError:
        # Retourne False si le fichier CSV n'existe pas
        return False

    try:
        # Ouverture du fichier JSON en mode écriture
        with open("data.json", "w", encoding="utf-8") as f:
            # Conversion et écriture des données en JSON avec indentation
            json.dump(data, f, indent=4)
        # Succès de la conversion
        return True
    except Exception:
        # Échec de l'écriture JSON
        return False
