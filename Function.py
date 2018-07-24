from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world 4"


@app.route("/vova")
def index():
    return "Hello vova 4"
