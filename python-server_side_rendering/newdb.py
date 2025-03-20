import sqlite3

def create_database():
    # Connexion à la base de données (crée le fichier s'il n'existe pas)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Suppression de la table si elle existe déjà pour éviter les doublons
    cursor.execute('DROP TABLE IF EXISTS Products')
    
    # Création de la table Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insertion des données d'exemple
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    # Validation des changements et fermeture de la connexion
    conn.commit()
    print("Base de données créée avec succès avec 2 produits.")
    conn.close()

if __name__ == '__main__':
    create_database()