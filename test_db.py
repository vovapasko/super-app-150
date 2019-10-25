import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import credentials


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

    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def fetchUserByName(self):
        meta = MetaData()
        customer = Table('customer', meta,
                         Column('name'),
                         Column('age'),
                         Column('email'),
                         Column('address'),
                         Column('zip_code'))

        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchAllUsers(self):
        # bind an individual Session to the connection
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)

    def saveData(self, customer):
        session = Session(bind=self.connection)
        session.add(customer)
        session.commit()

    def updateCustomer(self, customerName, address):
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        customerData = session.query(Customer).filter(Customer.name == customerName)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self, customer_id):
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.id == customer_id).first()
        session.delete(customerData)
        session.commit()


# class Customer():
#     def __init__(self, name, age, email, address, zip_code):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.address = address
#         self.zip_code = zip_code
#

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Customer(name='%s', age='%s', email='%s', address='%s', zip code='%s')>" % (
            self.name, self.age, self.email, self.address, self.zip_code)


db = Database()
# # db.fetchAllUsers()
# customer = Customer(name="Felipe Test", age=23, email="felipetest@gmail.com",
#                     address="Felipe Test Address", zip_code="2323LF")
# db.updateCustomer("Felipe Test", "new address updating")
# db.saveData(customer)
# db.deleteCustomer(9)
