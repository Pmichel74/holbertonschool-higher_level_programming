#!/usr/bin/python3
"""
    Définition de la classe State et déclaration de Base
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Création de l'instance de Base
Base = declarative_base()


class State(Base):
    """
        Classe State qui représente la table states dans la base de données

        Attributes:
            id (int): Identifiant unique auto-généré et clé primaire
            name (str): Nom de l'état, longueur max 128 caractères
    """
    # Nom de la table à laquelle la classe est liée
    __tablename__ = 'states'

    # Définition des colonnes
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Création de l'engine SQLAlchemy pour la connexion à MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],  # Username
            sys.argv[2],  # Password
            sys.argv[3]   # Database name
        ),
        pool_pre_ping=True  # Vérifie si la connexion est active avant utilisation
    )
    # Crée les tables dans la base de données selon les modèles définis
    Base.metadata.create_all(engine)
