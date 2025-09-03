from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bereken_batterijcapaciteit():
    if request.method == 'POST':
        try:
            verbruik_huis = float(request.form.get("huisverbruik"))
            verbruik_auto = float(request.form.get("autoverbruik"))
            opbrengst_panelen = float(request.form.get("zonnepanelen"))
            
            totaal_verbruik = verbruik_huis + verbruik_auto
            
            nodig_uit_batterij = totaal_verbruik - opbrengst_panelen
            
            batterij_capaciteit = max(0, nodig_uit_batterij * 1.2)
            
            return render_template('index.html', resultaat=f"{batterij_capaciteit:.2f} kWh")
            
        except (ValueError, TypeError):
            return render_template('index.html', foutmelding="Voer geldige getallen in.")
        
    return render_template('index.html', resultaat=None)

if __name__ == '__main__':
    app.run(debug=True)
