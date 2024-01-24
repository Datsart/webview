import sqlite3


def create_db_func():
    connection = sqlite3.connect('users_info_database.db')
    cursor = connection.cursor()
    print('Создана новая БД')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_info_table (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    timestamp DATETIME
    )
    ''')
    print('Создана новая таблица')
    connection.commit()
    # connection.close()
# create_db_func()