from flask import Flask, render_template, request

app = Flask(__name__)

# Route principale pour afficher la page de la calculatrice
@app.route('/')
def index():
    return render_template('index.html')

# Route pour calculer le résultat
@app.route('/calculer', methods=['POST'])
def calculer():
    try:
        # Récupérer les données du formulaire
        nombre1 = float(request.form['nombre1'])
        nombre2 = float(request.form['nombre2'])
        operation = request.form['operation']

        # Effectuer l'opération
        if operation == 'addition':
            resultat = nombre1 + nombre2
        elif operation == 'soustraction':
            resultat = nombre1 - nombre2
        elif operation == 'multiplication':
            resultat = nombre1 * nombre2
        elif operation == 'division':
            if nombre2 != 0:
                resultat = nombre1 / nombre2
            else:
                return "Erreur : Division par zéro !"
        else:
            return "Opération inconnue !"
        
        return render_template('index.html', resultat=resultat)
    
    except ValueError:
        return "Entrée non valide, veuillez saisir des nombres."

if __name__ == '__main__':
    app.run(debug=True)
