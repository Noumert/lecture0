from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world 7"


@app.route("/<string:name>")
def hello(name):
    return render_template("Pade.html")
