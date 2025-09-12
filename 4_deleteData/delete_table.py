import sqlite3

connection = sqlite3.connect('mydatabase.db')
connection.execute('DROP TABLE books')
connection.commit()
connection.close()