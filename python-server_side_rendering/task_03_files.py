from flask import Flask, render_template, request
import json
import csv
import os

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


@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
        items = data.get('items', [])
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Retourner juste la liste des produits si elle est dans une clé "products"
        if isinstance(data, dict) and "products" in data:
            return data["products"]
        return data


def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Vérifier si la source est valide
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Déterminer le chemin du fichier
    file_path = f"products.{source}"
    
    # Vérifier si le fichier existe
    if not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")
    
    try:
        # Charger les données selon la source
        if source == 'json':
            products_data = read_json(file_path)
        else:  # CSV
            products_data = read_csv(file_path)
        
        # Filtrer par ID si fourni
        if product_id:
            try:
                product_id = int(product_id)
                filtered_products = [p for p in products_data if p['id'] == product_id]
                if not filtered_products:
                    return render_template('product_display.html', error="Product not found")
                products_data = filtered_products
            except ValueError:
                return render_template('product_display.html', error="Invalid product ID")
        
        # Passer les produits au template
        return render_template('product_display.html', products=products_data)
    
    except Exception as e:
        # Capture les autres erreurs
        return render_template('product_display.html', error=f"An error occurred: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
