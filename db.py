import sqlite3
import seed
# import time
# import datetime


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

    @classmethod
    def deleteItem(cls, colId, rowNum):
        print('deleting', str(colId), '-', str(rowNum))
        cls.openConn()
        cls.cursor.execute('SELECT * FROM items WHERE colId = ?', (colId,))
        try:
            data = cls.cursor.fetchall()[rowNum-1]
            cls.cursor.execute('DELETE FROM items WHERE itemId = ?',
                               (data[0],))
            cls.conn.commit()
        except IndexError:
            print("Item does not exist!\n")
        cls.closeConn()

    @classmethod
    def addItem(cls, colId, todo, priority=5):
        cls.openConn()
        cls.cursor.execute('INSERT INTO items (colId, kanId, todo, priority)'
                           ' VALUES (?, ?, ?, ?)', (colId, 1, todo, priority))
        cls.conn.commit()


def main():
    seed.main()
    data = Db.read()
    print(data)
    Db.addItem('hello', 6)

    data = Db.read()
    print(data)
    # Db.deleteItem(2, 3)


if __name__ == "__main__":
    main()
