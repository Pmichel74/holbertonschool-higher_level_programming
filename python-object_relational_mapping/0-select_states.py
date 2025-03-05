#!/usr/bin/python3
"""
    Script qui liste tous les états de la base de données.
"""
import MySQLdb
import sys  # Module pour accéder aux arguments de la ligne de commande


def connectDb(user, password, db):
    """
    Se connecte à la base de données MySQL et retourne la connexion.

    Arguments:
        user (str): Nom d'utilisateur MySQL
        password (str): Mot de passe MySQL
        db (str): Nom de la base de données

    Retourne:
        Connection: Connexion à la base de données MySQL
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db
    )
    return connection


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Établir la connexion à la base de données
    db = connectDb(username, password, database)

    # Créer un curseur
    cursor = db.cursor()

    # Exécuter une requête pour sélectionner tous les états
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Afficher les résultats
    for row in results:
        print(row)
    cursor.close()
    db.close()
