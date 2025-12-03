-- Students table

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL CHECK (birth_year >= 1900)
);

-- Grades table

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Indexes

CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);

-- Insert students data

INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Insert grades data
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
    (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
    (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
    (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
    (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
    (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
    (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
    (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
    (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);

-- Queries

-- All grades for Alice Johnson
SELECT s.id, s.full_name, s.birth_year,
       GROUP_CONCAT(g.subject || ': ' || g.grade, ', ') AS grades
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
GROUP BY s.id;

-- Average grade for each student

SELECT s.id, s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade IS NOT NULL
GROUP BY s.id
ORDER BY avg_grade DESC;

-- Students born after 2004

SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004

ORDER BY birth_year;

-- Average grade per subject

SELECT subject, AVG(grade) AS avg_grade
FROM grades
WHERE grade IS NOT NULL

GROUP BY subject
ORDER BY avg_grade DESC;

-- Top 3 students by average grade

SELECT s.id, s.full_name, AVG(g.grade) AS avg_grade

FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade IS NOT NULL
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;

-- Students with at least one grade below 80

SELECT DISTINCT s.id, s.full_name, s.birth_year
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.id;
