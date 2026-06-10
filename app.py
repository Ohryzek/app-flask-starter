from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # Přidán POST, aby fungoval formulář
def index():
    # aktuální datum
    date = datetime.now().strftime("%d. %m. %Y")
    error = None
    name = None
    surname = None

    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")

        # VALIDACE VSTUPU
        if not name or name.strip() == "":
            error = "Chyba: Jméno nesmí být prázdné."
            name = None # Vymažeme jméno, aby se nevypsal pozdrav
        elif len(name) > 50:
            error = "Chyba: Jméno nesmí být delší než 50 znaků."
            name = None
    else:
        # Původní kód pro GET požadavky (např. heslo v URL)
        password = request.args.get("password")
        if password == "tajneheslo":
            return "Tajné heslo je správné!"
        elif password:
            return "Tajné heslo je nesprávné!"
        name = request.args.get("name")
        surname = request.args.get("surname")

    # Přidáno předání proměnné 'error' do šablony
    return render_template("page.html", date=date, name=name, surname=surname, error=error)      

@app.route("/pozdrav-post", methods=["POST", "GET"])
def pozdrav_post():
    # aktuální datum
    date = datetime.now().strftime("%d. %m. %Y")
    error = None
    name = None
    surname = None
    secret = None
    
    # Správné heslo
    SPRAVNE_HESLO = "python123"

    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        password = request.form.get("password", "")

        # VALIDACE VSTUPU
        # 1. Ošetři prázdné jméno
        if not name or name.strip() == "":
            error = "Chyba: Zadej prosím své jméno, pole nesmí zůstat prázdné."
            name = None
        # 2. Omez délku jména na 50 znaků
        elif len(name) > 50:
            error = "Chyba: Zadané jméno je příliš dlouhé (maximálně 50 znaků)."
            name = None
        # 3. Kontrola hesla (pokud je vyplněno)
        elif password and password != SPRAVNE_HESLO:
            error = "Chyba: Zadané heslo je nesprávné."
        elif password == SPRAVNE_HESLO:
            secret = "Gratulujeme! Jsi vítěz! 🏆 Tajné číslo: 42"

    # Přidáno předání proměnné 'secret' do šablony
    return render_template("pozdrav_post.html", date=date, name=name, surname=surname, error=error, secret=secret)

if __name__=="__main__":
    app.run(debug=True)