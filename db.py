import sqlite3
import seed
import time
import datetime


class Db():

    # def __init__(self):
        #  On initialization, connect to local db

    # Creates a table called stuff with the columns as listed
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL,\
                            datestamp TEXT, keyword TEXT, value REAL)')

    @classmethod
    def read(cls):
        cls.openConn()
        cls.cursor.execute('SELECT * FROM kanbans')
        kanTbl = cls.cursor.fetchall()

        cls.cursor.execute('SELECT * FROM columns WHERE kanId = ?',
                           (kanTbl[0][0],))
        colTbl = cls.cursor.fetchall()

        cls.cursor.execute('SELECT * FROM items WHERE kanId = ?', (1,))
        itemTbl = cls.cursor.fetchall()

        data = (kanTbl, colTbl, itemTbl)

        cls.closeConn()
        print("Loading")
        return data

    @classmethod
    def openConn(cls):
        cls.conn = sqlite3.connect('kan.db')
        cls.cursor = cls.conn.cursor()

    @classmethod
    def closeConn(cls):
        cls.cursor.close()
        cls.conn.close()

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
    data = Db.read()
    print(data)


if __name__ == "__main__":
    main()
