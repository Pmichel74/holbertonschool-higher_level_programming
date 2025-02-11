#!/usr/bin/python3
# Import du module ElementTree pour manipuler le XML
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Args:
    - dictionary (dict): Python dictionary to serialize.
    - filename (str): Filename to save the XML data.

    Returns:
    - None
    """
    # Création de l'élément racine 'data'
    root = ET.ElementTree('data')

    # Parcours des paires clé-valeur du dictionnaire
    for key, value in dictionary.items():
        # Création d'un sous-élément pour chaque clé
        child = ET.SubElement(root, key)
        # Définition du texte de l'élément comme la valeur convertie en string
        child.text = str(value)

    # Création de l'arbre XML final
    tree = ET.ElementTree(root)
    # Écriture de l'arbre dans le fichier
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
    - filename (str): Filename from which to read XML data.

    Returns:
    - dict: Deserialized Python dictionary.
    """
    # Lecture et analyse du fichier XML
    tree = ET.parse(filename)
    # Récupération de l'élément racine
    root = tree.getroot()

    # Dictionnaire pour stocker les données désérialisées
    result = {}
    # Parcours des éléments enfants de la racine
    for child in root:
        # Stockage de la paire tag:text dans le dictionnaire
        result[child.tag] = child.text

    return result
