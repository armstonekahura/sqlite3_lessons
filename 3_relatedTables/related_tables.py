import sqlite3

connection = sqlite3.connect('mydatabase.db')
connection.execute('''
    CREATE TABLE IF NOT EXISTS Students(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name Text,
                       age INTEGER
                       )
''')

connection.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   course_name Text,
                   student_id INTEGER,
                   FOREIGN KEY(student_id) REFERENCES Students(id)
                   )
''')

students_data = [
    ("Armstone", 18),
    ("Mary", 34),
    ("Eddie", 49),
]

courses_data = [
    ("Linear Algebra", 1),
    ("OOP", 2),
    ("IoT", 3),
]

# connection.executemany('INSERT INTO Students(name, age) VALUES(?,?)', students_data)
# connection.executemany('INSERT INTO Courses (course_name, student_id) VALUES(?,?)', courses_data)

results = connection.execute('''
                             SELECT Students.name, Courses.course_name
                             FROM Students
                             INNER JOIN Courses ON Students.id = Courses.student_id
                             ''')

connection.commit()

print("Student - Course Relationship")
for row in results.fetchall():
    print(f'Student: {row[0]}, Course: {row[1]}')
connection.close()