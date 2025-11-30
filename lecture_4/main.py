import sqlite3

# Connect to the database (creates school.db if it doesn't exist)
db = sqlite3.connect("school.db")
c = db.cursor()

# ---------------------------------------------------------
# TABLE CREATION AND DATA INSERTION (commented out)
# ---------------------------------------------------------
# These commands are only needed once when initializing the database.
# After the tables are created and filled, you should keep them commented.

# c.execute("DROP TABLE IF EXISTS students")
# c.execute("DROP TABLE IF EXISTS grades")

# Create the students table
# c.execute("""
# CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     full_name TEXT,
#     birth_year INTEGER
# )
# """)

# List of students
# students = [
#     ('Alice Johnson', 2005),    
#     ('Brian Smith', 2004), 
#     ('Carla Reyes', 2006), 
#     ('Daniel Kim', 2005), 
#     ('Eva Thompson', 2003), 
#     ('Felix Nguyen', 2007), 
#     ('Grace Patel', 2005),
#     ('Henry Lopez', 2004),
#     ('Isabella Martinez', 2006)
# ]

# Insert students into the table
# c.executemany("""
# INSERT INTO students (full_name, birth_year)
# VALUES (?, ?)
# """, students)

# Delete all students (use only if you want to clear the table)
# c.execute("DELETE FROM students")
# db.commit()

# ---------------------------------------------------------
# Same for the grades table (creation + insertion)
# ---------------------------------------------------------

# grades = [
#     (1, 'Math', 88),
#     (1, 'English', 92), 
#     (1, 'Science', 85),
#     (2, 'Math', 75),
#     (2, 'History', 83), 
#     (2, 'English', 79),
#     (3, 'Science', 95),
#     (3, 'Math', 91),
#     (3, 'Art', 89),
#     (4, 'Math', 84),
#     (4, 'Science', 88),
#     (4, 'Physical Education', 93),
#     (5, 'English', 90),
#     (5, 'History', 85),
#     (5, 'Math', 88),
#     (6, 'Science', 72), 
#     (6, 'Math', 78), 
#     (6, 'English', 81),
#     (7, 'Art', 94),
#     (7, 'Science', 87),
#     (7, 'Math', 90), 
#     (8, 'History', 77), 
#     (8, 'Math', 83),
#     (8, 'Science', 80),
#     (9, 'English', 96),
#     (9, 'Math', 89), 
#     (9, 'Art', 92)
# ]

# Insert grades
# c.executemany("""
# INSERT INTO grades (id_student, subject, grade)
# VALUES (?, ?, ?)
# """, grades)
# db.commit()

# ---------------------------------------------------------
# SQL QUERIES
# ---------------------------------------------------------

# 1. All grades for Alice Johnson
c.execute("""
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.id_student = s.id
WHERE s.full_name = 'Alice Johnson'
""")
print(f"Alice Johnson grades: {c.fetchall()}\n")

# 2. Average grade for each student
c.execute("""
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.id_student
GROUP BY s.id
""")
print(f"Average score for each student: {c.fetchall()}\n")

# 3. Students born after 2004
c.execute("""
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004
""")
print(f"Students born after 2004: {c.fetchall()}\n")

# 4. Average grade for each subject
c.execute("""
SELECT subject, ROUND(AVG(grade), 2) AS average_grade
FROM grades
GROUP BY subject
""")
print(f"Average score for each subject: {c.fetchall()}\n")

# 5. Top 3 students with the highest GPA
c.execute("""
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.id_student
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3
""")
print(f"Top 3 students with the highest GPA: {c.fetchall()}\n")

# 6. Students who scored below 80 in any subject
c.execute("""
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.id_student
WHERE g.grade < 80
""")
print(f"Students who received < 80 in at least one subject: {c.fetchall()}")

# Close the database connection
db.close()
