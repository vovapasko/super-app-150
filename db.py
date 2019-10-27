import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import credentials
from entities import Player


class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    cstr = 'postgresql://{user}:{password}@{hostname}/{database}'.format(
        user=credentials.username,
        password=credentials.password,
        hostname=credentials.host,
        database=credentials.database
    )
    engine = db.create_engine(cstr)

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def createPlayer(self, player):
        session = Session(bind=self.connection)
        session.add(player)
        session.commit()
        print("Player created successfully!")

    def updatePlayer(self, player_id, player_balance, player_passwd):
        session = Session(bind=self.connection)
        dataToUpdate = {Player.balance: player_balance, Player.passwrd: player_passwd}
        playerData = session.query(Player).filter(Player.player_id == player_id)
        playerData.update(dataToUpdate)
        session.commit()
        print("Player updated successfully!")

    def fetchAllPlayers(self):
        self.session = Session(bind=self.connection)
        players = self.session.query(Player).all()
        return players

    def deletePlayer(self, player_id):
        session = Session(bind=self.connection)
        playerData = session.query(Player).filter(Player.player_id == player_id).first()
        session.delete(playerData)
        session.commit()
        print("Player deleted successfully!")

