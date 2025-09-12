import sqlite3

connection = sqlite3.connect('mydatabase.db')

# delete a specific book by its id from the books table
book_id_to_delete = 1
connection.execute('DELETE FROM books WHERE id = ?', (book_id_to_delete,))

connection.commit()

result = connection.execute('SELECT * FROM books')

print("Books")

for row in result.fetchall():
    print(f'Title: {row[1]}, Author: {row[2]}, YoP: {row[3]}')

connection.close()