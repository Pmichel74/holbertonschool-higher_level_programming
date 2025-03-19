from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Récupérer les paramètres de la requête
    source = request.args.get('source')
    item_id = request.args.get('id')
    
    data = []
    error = None
    
    # Charger les données selon le paramètre source
    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            error = f"Erreur lors du chargement du fichier JSON: {str(e)}"
    
    elif source == 'csv':
        try:
            with open('products.csv', 'r', newline='') as file:
                csv_reader = csv.DictReader(file)
                data = list(csv_reader)
        except FileNotFoundError as e:
            error = f"Erreur lors du chargement du fichier CSV: {str(e)}"
    
    else:
        error = "Wrong source"
    
    # Filtrer par ID si spécifié et s'il n'y a pas d'erreur
    if item_id and not error:
        filtered_data = [item for item in data if str(item.get('id')) == str(item_id)]
        if not filtered_data:
            error = "Product not found"
        else:
            data = filtered_data
    
    # Passer les données et les éventuelles erreurs au template pour l'affichage
    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
