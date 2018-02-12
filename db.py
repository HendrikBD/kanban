import sqlite3
import time
import datetime
import random


# Defines the database as a file at the specified location (.db)
conn = sqlite3.connect('data.db')

# create a cursor, which points to a specific place in the database
c = conn.cursor()


# Creates a table called stuff with the columns as listed
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, \
                  keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuff VALUES(145, '2018-02-05', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()  # Stops memory from being used for the connection


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:'
                                                              '%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuff (unix, datestamp, keyword, value) VALUES (?, '
              '?, ?, ?)', (unix, date, keyword, 2))
    conn.commit()


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


# create_table()
# data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
# read_from_db()
# print(79*"#")
# sqlite_update()
sqlite_delete()
# read_from_db()
c.close()
conn.close()
