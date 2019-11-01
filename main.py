import flask
from flask import Flask, render_template

from db import Database

app = Flask(__name__)

database = Database()

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/players')
def players():
    all_players = database.fetchAllPlayers()
    return render_template("players.html", all_players=all_players)


@app.route('/players/<player_id>')
def update_player(player_id):
    return render_template()

@app.route('/bets')
def bets():
    all_bets = database.fetchAllBets()
    return render_template("bet.html", all_bets=all_bets)


@app.route('/banks')
def banks():
    all_banks = database.fetchAllBanks()
    return render_template("bank.html", all_banks=all_banks)


if __name__ == '__main__':
    app.run(debug=True)
