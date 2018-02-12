import sqlite3

conn = sqlite3.connect('kan.db')
curs = conn.cursor()
tables = ['kanbans', 'categories', 'items']


def seed():
    createTable()
    #  Adding kanban
    curs.execute("INSERT INTO kanbans (name, active, createdate) VALUES \
                 ('ToDo', 1, 42)")

    #  Adding categories
    curs.execute("INSERT INTO categories (kanId, name) VALUES (42, 'ToDo')")
    curs.execute("INSERT INTO categories (kanId, name) VALUES (42, 'Plan')")
    curs.execute("INSERT INTO categories (kanId, name) VALUES (42, 'Doing')")
    curs.execute("INSERT INTO categories (kanId, name) VALUES (42, 'Done')")

    # Adding items

    curs.execute("INSERT INTO items (catId, kanId, name) VALUES (1, 4, 'Tst')")
    print('Created db')


def createTable():
    curs.execute('CREATE TABLE IF NOT EXISTS kanbans (kanId INTEGER PRIMARY \
                 KEY AUTOINCREMENT, name TEXT, active REAL, createdate REAL)')
    curs.execute('CREATE TABLE IF NOT EXISTS categories (catId INTEGER \
                 PRIMARY KEY AUTOINCREMENT, kanId REAL, name TEXT)')
    curs.execute('CREATE TABLE IF NOT EXISTS items (itemId INTEGER PRIMARY \
                 KEY AUTOINCREMENT, catId REAL, kanId REAL, name TEXT)')


def dropTables():
    curs.execute('DROP TABLE IF EXISTS kanbans')
    curs.execute('DROP TABLE IF EXISTS categories')
    curs.execute('DROP TABLE IF EXISTS items')


def checkTables():
    #  Returns table if it exists:
    #  print(curs.execute('SELECT name FROM sqlite_master WHERE type="table"
    #  AND name="kanbans"'))
    for i in range(0, 3):
        print(i)
        curs.execute('SELECT * FROM %s' % tables[i])
        [print(row) for row in curs.fetchall()]


def main():
    seed()
    checkTables()
    dropTables()
    curs.execute('SELECT name FROM sqlite_master WHERE type="table" AND \
                 name="kanbans"')
    print('\n', curs.fetchall())

    curs.close()
    conn.close()


if __name__ == "__main__":
    main()
