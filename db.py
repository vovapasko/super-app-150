import psycopg2

import credentials

connection = psycopg2.connect(database='MyDb', user=credentials.username, password=credentials.password)

cursor = connection.cursor()
cursor.execute('''SELECT * FROM CLIENT;''')
print(cursor.fetchall())
connection.close()


