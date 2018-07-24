import datetime

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    headLine0 = now.year
    headLine1 = now.month
    headLine2 = now.day
    headLine3 = now.hour
    headLine4 = now.minute
    headLine5 = now.second
    return render_template("hello.html", headLine0=headLine0, headLine1=headLine1, headLine2=headLine2,
                           headLine3=headLine3, headLine4=headLine4, headLine5=headLine5)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
