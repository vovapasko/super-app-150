from sqlalchemy import TIMESTAMP

from db import Database
from entities import Bank, Bet

db = Database()
# player = Player(player_id=12345, balance=8500242, passwrd="passwdVasya")
# db.createPlayer(player)
# players = db.fetchAllPlayers()
# print(players)
# db.updatePlayer(12345, 0, "passwdPetya")
# db.delete_casino(300)
# db.delete_username(300)
# db.deleteBank(300)
# db.deletePlayer(300)
# bank
# bank = Bank(player_id=100, sold_time='2016-06-22 19:10:25-07', sold_coins=123412987)
# db.createBank(bank)
# db.updateBankWithTime(100, '2016-06-22 19:10:25-07', 0)
# db.deleteBank(100)
#bet
# bet = Bet(bet_id=4, bet_money=123.45, won_money=2000, won_bet=True, bet_time='2016-06-22 19:10:25-07')
# db.createBet(bet)
db.deleteBank(250)
