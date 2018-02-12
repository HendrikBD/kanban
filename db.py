import sqlite3
import time
import datetime


# Defines the database as a file at the specified location (.db)
conn = sqlite3.connect('kan.db')

# create a cursor, which points to a specific place in the database
c = conn.cursor()


# Creates a table called stuff with the columns as listed
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, \
                  keyword TEXT, value REAL)')


def load(data):
    data = (42, [40, 41, 42, 43], "ToDoKan",
            ['ToDoKan', 'PlanKan', 'DoingKan', 'DoneKan'],
            [51, 52], ['Do one thing', 'Do another'], [5, 6],
            [53, 54], ['Hello?', 'World'], [5, 6],
            [55, 56], ['Why?', 'Me?'], [5, 6],
            [57, 58], ['Goodbye?', 'all'], [5, 6])
    print("Loading")
    print(data)
    return data


def data_entry():
    c.execute("INSERT INTO stuff VALUES(145, '2018-02-05', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()  # Stops memory from being used for the connection


def read_from_db():
    c.execute('SELECT * FROM stuff')
    [print(row) for row in c.fetchall()]


def sqlite_update():
    c.execute('SELECT * FROM stuff')
    c.execute('Update stuff SET value = 99 WHERE value=8')
    conn.commit()


def sqlite_delete():
    c.execute('SELECT * FROM stuff WHERE value = 2')
    print(len(c.fetchall()))
    # conn.commit()


c.close()
conn.close()
