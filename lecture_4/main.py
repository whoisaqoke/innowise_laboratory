import os
import sqlite3

DB_NAME = "school.db"

def connect_db():
    """Устанавливает соединение с базой данных и включает поддержку внешних ключей."""
    
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def setup_database():
    """Создаёт базу данных и таблицы, если они отсутствуют."""

    if os.path.isfile(DB_NAME):
        print(" База данных уже существует.")
        return False

    conn = connect_db()
    cursor = conn.cursor()

    # Таблица студентов
    
    cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            birth_year INTEGER NOT NULL CHECK (birth_year >= 1900)
        )
    """)

    # Таблица оценок
    
    cursor.execute("""
        CREATE TABLE grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            grade INTEGER CHECK (grade BETWEEN 1 AND 100),
            FOREIGN KEY (student_id) REFERENCES students(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    """)

    # Первичные данные
    
    cursor.executemany(
        "INSERT INTO students (full_name, birth_year) VALUES (?, ?)",
        [
            ('Alice Johnson', 2005),
            ('Brian Smith', 2004),
            ('Carla Reyes', 2006),
            ('Daniel Kim', 2005),
            ('Eva Thompson', 2003),
            ('Felix Nguyen', 2007),
            ('Grace Patel', 2005),
            ('Henry Lopez', 2004),
            ('Isabella Martinez', 2006),
        ]
    )

    cursor.executemany(
        
        "INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
       
        [
            (1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
            (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
            (3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
            (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
            (5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
            (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
            (7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
            (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
            (9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92),
        ]
    )

    # Индексы для ускорения запросов
    cursor.execute("CREATE INDEX idx_student ON grades(student_id)")
    cursor.execute("CREATE INDEX idx_subject ON grades(subject)")

    conn.commit()
    conn.close()

    print(f"[INFO] База данных '{DB_NAME}' успешно создана и готова к работе.")
    return True

def init_db():
    """Проверяет наличие базы и открывает соединение."""

    created = setup_database()

    if created:
        print("Продолжаем выполнение после создания базы.")
    
    else:
        print("Используем существующую базу данных.")

    conn = connect_db()
    print(" Соединение установлено.")
    conn.close()
    print("Соединение закрыто.")

if __name__ == "__main__":
    init_db()
