#!/usr/bin/python3
"""
Script qui liste tous les objets State contenant la lettre 'a'
dans la base de données hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Création de l'engine SQLAlchemy pour la connexion à MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
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

    # Récupération des objets State contenant la lettre 'a' dans leur nom
    # Triés par ID croissant
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Affichage des résultats au format demandé
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture de la session
    session.close()
