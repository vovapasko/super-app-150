from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import TIMESTAMP


cstr = 'postgresql://{user}:{password}@{sid}'.format(
    user='postgres',
    password='postgres',
    sid='MyDb'
)

engine = create_engine(
    cstr,
    convert_unicode=False,
    echo=True
)

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"
    player_id = Column(Integer, primary_key=True)
    balance = Column(Integer, nullable=False)
    passwrd = Column(String(64), nullable=False)


class Bank(Base):
    __tablename__ = "bank"
    player_id = Column(Integer, ForeignKey(Player.player_id), primary_key=True)
    sold_time = Column(TIMESTAMP, primary_key=True)
    sold_coins = Column(Float, nullable=False)


class Bet(Base):
    bet_id = Column(Integer, primary_key=True)
    bet_money = Column(Float, nullable=False)
    won_money = Column(Float, nullable=False)
    won_bet = Column(Boolean, nullable=False)
    bet_time = Column(TIMESTAMP, nullable=False)



Base.metadata.create_all(engine)

session = Session()
new_player = Player(player_id=123, player_balance=180000, passwrd="passwrd")


