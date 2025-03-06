#!/usr/bin/python3
"""
Script qui affiche le premier objet State de la base de données hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Création de l'engine SQLAlchemy pour la connexion à MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],  # Username
            sys.argv[2],  # Password
            sys.argv[3]   # Database name
        ),
        pool_pre_ping=True  # Vérifie la connexion avant utilisation
    )

    # Création d'une classe Session liée à notre engine
    Session = sessionmaker(bind=engine)

    # Création d'une instance de Session pour interagir avec la base de données
    session = Session()

    # Création des tables dans la base de données
    Base.metadata.create_all(engine)

    # Récupération du premier objet State par ID
    first_state = session.query(State).order_by(State.id).first()

    # Affichage du résultat ou "Nothing" si aucun État n'est trouvé
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Fermeture de la session
    session.close()
