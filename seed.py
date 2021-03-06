import sqlite3
import time

tables = ['kanbans', 'columns', 'items']
conn = sqlite3.connect('kan.db')
curs = conn.cursor()


def seed():
    createTable()
    initTable()

    # Adding items
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(1, 1, 'Some really really long statement. Bro.', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(3, 1, 'That one thing', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(1, 1, 'That other thing', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(2, 1, 'Something important, but what?', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(1, 1, 'coding', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(4, 1, 'coding', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(1, 1, 'coding', 5)")
    curs.execute("INSERT INTO items (colId, kanId, todo, priority) VALUES "
                 "(3, 1, 'Do Nothing', 5)")

    conn.commit()
    print('Tables have been seeded and commited!', end='\n\n')


def createTable():
    curs.execute('CREATE TABLE IF NOT EXISTS kanbans (kanId INTEGER PRIMARY '
                 'KEY AUTOINCREMENT, name TEXT, active INTEGER, createdate '
                 'INTEGER)')
    curs.execute('CREATE TABLE IF NOT EXISTS columns (colId INTEGER '
                 'PRIMARY KEY AUTOINCREMENT, kanId INTEGER, name TEXT)')
    curs.execute('CREATE TABLE IF NOT EXISTS items (itemId INTEGER PRIMARY '
                 'KEY AUTOINCREMENT, kanId INTEGER, colId, todo TEXT,'
                 ' priority INTEGER)')


def dropTables():
    curs.execute('DROP TABLE IF EXISTS kanbans')
    curs.execute('DROP TABLE IF EXISTS columns')
    curs.execute('DROP TABLE IF EXISTS items')


def checkTables():
    #  Returns table if it exists:
    #  print(curs.execute('SELECT name FROM sqlite_master WHERE type="table"
    #  AND name="kanbans"'))
    for i in range(0, 3):
        print(tables[i], ':', sep='')
        curs.execute('SELECT * FROM %s' % tables[i])
        [print(row) for row in curs.fetchall()]
        print()


def initTable():
    dropTables()
    createTable()
    unix = int(time.time())

    #  Adding kanban
    curs.execute("INSERT INTO kanbans (name, active, createdate) VALUES \
                 ('ToDo', 1, ?)", (unix,))

    #  Adding columns
    curs.execute("INSERT INTO columns (kanId, name) VALUES (1, 'ToDo')")
    curs.execute("INSERT INTO columns (kanId, name) VALUES (1, 'Plan')")
    curs.execute("INSERT INTO columns (kanId, name) VALUES (1, 'Doing')")
    curs.execute("INSERT INTO columns (kanId, name) VALUES (1, 'Done')")
    conn.commit()


def main():
    dropTables()
    initTable()

    # seed()
    checkTables()
    curs.close()
    conn.close()


if __name__ == "__main__":
    main()
