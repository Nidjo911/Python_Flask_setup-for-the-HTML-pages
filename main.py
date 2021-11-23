#Flask app.
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/lekcije")
def lekcije():
    return render_template("lekcije.html")

@app.route("/lorem")
def lorem():
    return render_template("lorem.html")

@app.route("/training")
def training():
    return render_template("training.html")

if __name__ == "__main__":
    app.run(use_reloader = True)
