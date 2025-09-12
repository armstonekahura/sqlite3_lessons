import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title Text,
                                author Text,
                                year INTEGER
                                )
                                ''')

#  insert data into table
books_data = [
    ("The Progamatic Programmer", "Andy Hunt", 1999),
    ("Head First Python", "Paul", "2010"),
    ("Automation Python", "AI", 2015),
    ("Fluent Python", "Luciano", 2015),
]

# connection.executemany('INSERT INTO books(title, author, year) VALUES(?,?,?)', books_data)

# query data from the table
result = connection.execute('SELECT * FROM books')
data = result.fetchall()

# display the data
for row in data:
    print(f'Title: {row[1]}')
    print(f'Author: {row[2]}')
    print(f'Year: {row[3]}')
    print('')

# Write the data to the file
connection.commit()

# close the database connection
connection.close()