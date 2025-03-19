"""Module containing python script for sending invitations"""
# Import pour vérifier l'existence de fichiers sans avoir besoin d'utiliser tout le module os
from os.path import exists


def generate_invitations(template, attendees_list):
    """
    Fonction qui génère des fichiers d'invitation personnalisés pour chaque participant.
    
    Args:
        template: Chaîne de caractères contenant le modèle d'invitation avec des marqueurs {name}, etc.
        attendees_list: Liste de dictionnaires, chacun contenant les infos d'un participant
    
    Returns:
        None: La fonction crée des fichiers mais ne retourne aucune valeur
    """

    # ---------- VALIDATION DES ENTRÉES ----------
    
    # Vérifie que le template est bien une chaîne de caractères
    if not isinstance(template, str):
        print("ERROR: template must be a string")
        return  # Sortie anticipée de la fonction en cas d'erreur

    # Vérifie que le template n'est pas vide
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Vérifie que la liste des participants est bien une liste
    if not isinstance(attendees_list, list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    # Vérifie que la liste des participants n'est pas vide
    if not attendees_list:
        print("No data provided, no output files generated.")
        return

    # Vérifie que chaque élément de la liste est un dictionnaire
    # La fonction all() renvoie True si toutes les conditions sont vraies
    if not all(isinstance(item, dict) for item in attendees_list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    # ---------- TRAITEMENT DES INVITATIONS ----------
    
    # Parcourt chaque participant avec un index commençant à 1
    for index, attendee in enumerate(attendees_list, start=1):
        # Crée une copie du template pour ce participant
        processed_template = template
        
        # Remplace chaque marqueur par sa valeur correspondante
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            # Crée le marqueur au format {key}
            placeholder = "{" + key + "}"
            # Récupère la valeur ou utilise "N/A" si absente/None
            value = attendee.get(key) or "N/A"
            # Remplace toutes les occurrences du marqueur par la valeur
            processed_template = processed_template.replace(placeholder, value)
        
        # ---------- CRÉATION DES FICHIERS ----------
        
        # Génère un nom de fichier unique pour ce participant
        output_filename = f"output_{index}.txt"
        
        # Vérifie si le fichier existe déjà pour éviter l'écrasement
        if not exists(output_filename):
            # Ouvre le fichier en mode écriture et le ferme automatiquement après usage
            with open(output_filename, "w") as file:
                # Écrit le contenu personnalisé dans le fichier
                file.write(processed_template)
        else:
            # Affiche un message d'erreur si le fichier existe déjà
            print(f"ERROR: file {output_filename} already exists")