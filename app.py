# <Zoui Omar - ZOUO28089600>
# Examen final pratique - Été 2023

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="", static_folder="static")

bonnes_reponses = {
    'q1': 'nav',
    'q2': 'font-weight',
    'q3': 'b',
    'q4': 'url',
    'q5': ['input', 'label']
}

# Route pour l'erreur 404 page non trouvée.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

# Route principale vers le questionnaire.
@app.route('/')
def index():
    return render_template('final.html')

# Route vers le calcul de la note qui redirige vers la page du résultat.
@app.route('/calcul_note', methods=['POST'])
def calcul_note():
    code_permanent = request.form.get('code')
    reponses = {key: request.form.getlist(key) for key in request.form.keys() if key != 'code'}

    resultat = 0
    corrections = []

    for question, reponse in reponses.items():
        if question in bonnes_reponses:
            bonne_reponse = bonnes_reponses[question]
            
            if isinstance(bonne_reponse, list):
                if sorted(reponse) == sorted(bonne_reponse):
                    resultat += 20
                    corrections.append(f"Question {question[-1]}: Bonne réponse.")
                else:
                    corrections.append(f"Question {question[-1]}: Mauvaise réponse.")
            else:
                if reponse == [bonne_reponse]:
                    resultat += 20
                    corrections.append(f"Question {question[-1]}: Bonne réponse.")
                else:
                    corrections.append(f"Question {question[-1]}: Mauvaise réponse.")

    message = f"Code permanent: {code_permanent}. Votre résultat est de {resultat} sur {len(bonnes_reponses)*20}."
    fichier_txt = f"{code_permanent}.txt"

    with open(fichier_txt, 'w') as file:
        for correction in corrections:
            file.write(correction + '\n')

    return render_template('resultat.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)