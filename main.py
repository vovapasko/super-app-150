import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/players')
def players():
    return render_template("players.html")


@app.route('/bets')
def bets():
    return render_template("bet.html")


@app.route('/banks')
def banks():
    return render_template("bank.html")


if __name__ == '__main__':
    app.run(debug=True)
