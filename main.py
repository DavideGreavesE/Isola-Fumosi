from bs4 import BeautifulSoup
import requests
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    url = "https://isoladeifumosi.airc.it/elaborati/285"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    progetto_elements = soup.find_all(string=lambda t: t and "Progetto" in t)
    progetto = progetto_elements[1].strip() if len(progetto_elements) > 1 else None

    scuola_element = soup.find(string=lambda t: t and "Scuola" in t)
    scuola = scuola_element.strip() if scuola_element else None

    voti_element = soup.find(string=lambda t: t and "Voti" in t)
    voti = int(voti_element.strip().split(":")[-1].strip()) if voti_element else None

    return render_template("home.html", progetto=progetto, scuola=scuola, voti=voti)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
