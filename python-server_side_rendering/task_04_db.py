from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier si la source est valide
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    try:
        products_data = []

        # Traiter les données selon la source
        if source == 'json':
            # Code existant pour JSON
            with open('products.json', 'r') as file:
                data = json.load(file)
                if isinstance(data, dict) and "products" in data:
                    products_data = data["products"]
                else:
                    products_data = data
          
        elif source == 'csv':
            # Code existant pour CSV
            with open('products.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convertir les types de données si nécessaire
                    if 'id' in row:
                        row['id'] = int(row['id'])
                    if 'price' in row:
                        row['price'] = float(row['price'])
                    products_data.append(row)
         
        elif source == 'sql':
            # Nouveau code pour SQLite
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if product_id:
                cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            else:
                cursor.execute('SELECT * FROM Products')
    
            products_data = [dict(row) for row in cursor.fetchall()]
            conn.close()

        # Filtrer par ID pour JSON et CSV
        if product_id and source != 'sql':
            try:
                product_id = int(product_id)
                filtered_data = [p for p in products_data if int(p['id']) == product_id]
                if not filtered_data:
                    return render_template('product_display.html', error="Product not found")
                products_data = filtered_data
            except ValueError:
                return render_template('product_display.html', error="Invalid product ID")

        # Vérifier si des produits ont été trouvés pour SQL
        if source == 'sql' and product_id and not products_data:
            return render_template('product_display.html', error="Product not found")
            
        # Passer les produits au template
        return render_template('product_display.html', products=products_data)

    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    except json.JSONDecodeError:
        return render_template('product_display.html', error="Invalid JSON file")
    except sqlite3.Error as e:
        return render_template('product_display.html', error=f"Database error: {str(e)}")
    except Exception as e:
        return render_template('product_display.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
