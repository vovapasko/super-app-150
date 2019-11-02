import flask
from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

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


@app.route('/players/update/<player_id>')
def update_player(player_id):
    return render_template("update_player.html", player_id=player_id)


@app.route('/players/delete_player/<player_id>', methods=["POST"])
def delete_player(player_id):
    database.deletePlayer(player_id)
    return redirect(url_for("players"))


@app.route('/bets')
def bets():
    all_bets = database.fetchAllBets()
    return render_template("bet.html", all_bets=all_bets)


@app.route('/bets/<bet_id>')
def update_bet(bet_id):
    return render_template("update_bet.html", bet_id=bet_id)

@app.route('/bets/delete_bet/<bet_id>', methods=["POST"])
def delete_bet(bet_id):
    database.deleteBet(bet_id)
    return redirect(url_for("bets"))

@app.route('/banks')
def banks():
    all_banks = database.fetchAllBanks()
    return render_template("bank.html", all_banks=all_banks)


@app.route('/banks/<player_id>/<sold_time>')
def update_bank(player_id, sold_time):
    return render_template("update_bank.html", player_id=player_id, sold_time=sold_time)


@app.route('/banks/delete_bank/<player_id>/<sold_time>', methods=["POST"])
def delete_bank(player_id, sold_time):
    database.deleteBank(player_id, sold_time)
    return redirect(url_for("banks"))


if __name__ == '__main__':
    app.run(debug=True)
