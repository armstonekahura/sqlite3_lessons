import sqlite3

connection = sqlite3.connect('lesson1.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title Text,
                                author Text,
                                year INTEGER
                                )
                                ''')

# Write the data to the file
connection.commit()

# close the database connection
connection.close()