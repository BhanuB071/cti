import sqlite3

DATABASE = 'cti.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
sql_query = """ CREATE TABLE student_grades (
    id integer PRIMARY KEY,
    name text NOT NULL,
    course text NOT NULL,
    grade integer NOT NULL
    ) """
cursor.execute(sql_query)