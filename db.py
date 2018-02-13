import sqlite3
import seed
import time
import datetime


class Db():

    # cursor = []

    def __init__(self):
        # Defines the database as a file at the specified location (.db)
        self.conn = sqlite3.connect('kan.db')

        # create a cursor, which points to a specific place in the database
        self.cursor = self.conn.cursor()

    # Creates a table called stuff with the columns as listed
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL,\
                            datestamp TEXT, keyword TEXT, value REAL)')

    def read(self):
        self.cursor.execute('SELECT * FROM kanbans')
        kanTbl = self.cursor.fetchall()

        self.cursor.execute('SELECT * FROM columns WHERE kanId = ?',
                            (kanTbl[0][0],))
        colTbl = self.cursor.fetchall()

        self.cursor.execute('SELECT * FROM items WHERE kanId = ?', (1,))
        itemTbl = self.cursor.fetchall()

        data = (kanTbl, colTbl, itemTbl)

        print("Loading")
        return data

    def close(self):
        self.cursor.close()
        self.conn.close()

# def data_entry(conconnn):
#     c.execute("INSERT INTO stuff VALUES(145, '2018-02-05', 'Python', 5)")
#     conn.commit()
#     c.close()
#     conn.close()  # Stops memory from being used for the connection
# def sqlite_update():
#     c.execute('SELECT * FROM stuff')
#     c.execute('Update stuff SET value = 99 WHERE value=8')
#     conn.commit()
#
# def sqlite_delete():
#     c.execute('SELECT * FROM stuff WHERE value = 2')
#     print(len(c.fetchall()))
#     # conn.commit()

def main():
    seed.main()
    db = Db()
    data = db.read()
    print(data)
    db.close()


if __name__ == "__main__":
    main()
