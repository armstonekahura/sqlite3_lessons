import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS employees(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   employee_ID INTEGER,
                   name Text,
                   age INTEGER,
                   department Text
                   )
''')

employee_data = [
    (345, "Mary Gitau", 24, "Finance"),
    (678, "Armstone Strong", 54, "IT"),
    (987, "Phyllis Joy", 20, "Time Management"),
    (453, "Susan Gold", 29, "DCI"),
    (876, "Livingstone Maina", 24, "Interpol"),
    (871, "Brighton Leon", 43, "Finance"),
    (870, "Eddie Button", 54, "Transport"),
    (869, "Margaret Bill", 41, "Finance"),
    (868, "Mark Melita", 43, "Security"),
    (867, "Me McMain", 87, "Health")

]

connection.executemany('INSERT INTO employees (employee_ID, name, age, department) VALUES (?,?,?,?)', employee_data)

# query data from the table
result = connection.execute('SELECT * FROM employees ORDER BY age DESC')
data = result.fetchall()

# display the data
for row in data:
    print(f'employee_ID: {row[1]}')
    print(f'name: {row[2]}')
    print(f'age: {row[3]}')
    print(f'department: {row[4]}')
    print('')
connection.commit()
connection.close()