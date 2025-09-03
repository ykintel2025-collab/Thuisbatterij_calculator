import cgi

# Dit deel zorgt ervoor dat het script de gegevens van de HTML-formulier leest.
form = cgi.FieldStorage()

huisverbruik = float(form.getvalue("huisverbruik", 0))
autoverbruik = float(form.getvalue("autoverbruik", 0))
zonnepanelen = float(form.getvalue("zonnepanelen", 0))
extraverbruik = float(form.getvalue("extraverbruik", 0))

# De berekening
totaal_verbruik = huisverbruik + autoverbruik + extraverbruik
nodig_uit_batterij = totaal_verbruik - zonnepanelen

# Veiligheidsmarge toevoegen en zorgen dat het resultaat niet negatief is
batterij_capaciteit = max(0, nodig_uit_batterij * 1.2)

# De resultaten afdrukken naar de HTML-pagina
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head><title>Resultaat Batterijberekening</title></head>")
print("<body>")
print("<h1>Resultaat</h1>")
print(f"<p>Totaal dagelijks verbruik: {totaal_verbruik:.2f} kWh</p>")
print(f"<p>Opbrengst zonnepanelen: {zonnepanelen:.2f} kWh</p>")
print(f"<h2>Geschatte benodigde batterijcapaciteit: {batterij_capaciteit:.2f} kWh</h2>")
print("<a href='index.html'>Nieuwe berekening</a>")
print("</body>")
print("</html>")
