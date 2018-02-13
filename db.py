import sqlite3
import seed
# import time
# import datetime


class Db():

    isConnected = False
    stillActive = False

    # Creates a table called stuff with the columns as listed
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL,\
                            datestamp TEXT, keyword TEXT, value REAL)')

    @classmethod
    def openConn(cls):
        cls.conn = sqlite3.connect('kan.db')
        cls.cursor = cls.conn.cursor()
        cls.isConnected = True

    @classmethod
    def closeConn(cls):
        cls.cursor.close()
        cls.conn.close()
        cls.isConnected = False

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
    def addItem(cls, colId, todo, priority=5):
        if(not cls.isConnected):
            cls.openConn()
        cls.cursor.execute('INSERT INTO items (colId, kanId, todo, priority)'
                           ' VALUES (?, ?, ?, ?)', (colId, 1, todo, priority))
        cls.conn.commit()
        if(not cls.stillActive):
            cls.closeConn()

    @classmethod
    def moveItem(cls, colId, rowNum, newColId):
        cls.openConn()
        cls.stillActive = True
        try:
            cls.cursor.execute('SELECT * FROM items WHERE colId = ?', (colId,))
            cls.addItem(newColId, cls.cursor.fetchall()[rowNum-1][3])
            cls.deleteItem(colId, rowNum)
        except IndexError:
            print("That item does not exist!")
        cls.stillActive = False
        cls.closeConn()

    @classmethod
    def deleteItem(cls, colId, rowNum):
        if(not cls.isConnected):
            cls.openConn()
        cls.cursor.execute('SELECT * FROM items WHERE colId = ?', (colId,))
        try:
            data = cls.cursor.fetchall()[rowNum-1]
            cls.cursor.execute('DELETE FROM items WHERE itemId = ?',
                               (data[0],))
            cls.conn.commit()
        except IndexError:
            print("Item does not exist!\n")

        if(not cls.stillActive):
            cls.closeConn()


def main():
    seed.main()
    data = Db.read()
    print(data)

    Db.moveItem(1, 1, 4)

    data = Db.read()
    print(data)
    Db.deleteItem(4, 2)
    data = Db.read()
    print(data)


if __name__ == "__main__":
    main()
