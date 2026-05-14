from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


SPRAVNE_HESLO = "tajneheslo"

@app.route("/", methods=["GET"])
def index():
  
    date = datetime.now().strftime("%d. %m. %Y")
    return render_template("page.html", date=date)      

@app.route("/pozdrav-post", methods=["POST", "GET"])
def pozdrav_post():
    date = datetime.now().strftime("%d. %m. %Y")
    error = None
    name = None
    surname = None
    secret_info = None

    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        password = request.form.get("password")

   
        if not name or name.strip() == "":
            error = "Chyba: Zadej prosím své jméno, pole nesmí zůstat prázdné."
            name = None
        elif len(name) > 50:
            error = "Chyba: Zadané jméno je příliš dlouhé (maximálně 50 znaků)."
            name = None

     
        if password:
            if password == SPRAVNE_HESLO:
                secret_info = "Tohle je přísně tajná informace! Obědy na naší škole jsou super."
            else:
              
                if error:
                    error += " A navíc je zadané heslo nesprávné!"
                else:
                    error = "Chyba: Zadané heslo je nesprávné!"

    return render_template("pozdrav-post.html", date=date, name=name, surname=surname, error=error, secret_info=secret_info)

if __name__=="__main__":
    app.run(debug=True)