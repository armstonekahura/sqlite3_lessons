import sqlite3

connection = sqlite3.connect('mydatabase.db')
connection.execute('ALTER TABLE employees ADD COLUMN transport')

connection.commit()


connection.close()