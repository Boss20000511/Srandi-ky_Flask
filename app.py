from flask import Flask, render_template
from math import pi, sqrt

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("base.html.j2")


@app.route("/abc")
def abc():
    return render_template('abc.html.j2')


