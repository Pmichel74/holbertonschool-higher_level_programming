from flask import Flask, render_template
import json

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
        # Ouvre et charge le fichier JSON
        with open('items.json', 'r') as fichier:
            donnees = json.load(fichier)
        # Passe la liste d'items au template
        return render_template('items.html', items=donnees['items'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Gère les erreurs en passant une liste vide
        return render_template('items.html', items=[])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
