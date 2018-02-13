import seed
from db import Db


class Kanban():

    def __init__(self):
        data = Db.read()
        self.parse(data)

    def list(self):
        for col in eval("self.cols"):
            print(col)
            # for i in range(len(eval("self."+col+".items"))):
            #         print("  " + str(i+1) + ": " + eval("self." + col +
            #                                             ".items["+str(i)+"]"))
            #  List, optimized for terminal/general purpose

    def parse(self, data):
        print('Parsing')
        self.table = []
        self.columns = []
        self.kanId = data[0][0][0]
        self.name = data[0][0][1]

        for col in data[1]:
            self.table.append((col[2], col[0], []))

        for item in data[2]:
            self.table[item[2]-1][2].append(item[3])

    def addCol(self, colName):
        exec("self." + colName + "=self.column()")
        self.cols.append(colName)
        #  Add new category to tables with kanban id

    def addItem(self, colName, itemName):
        exec("self."+colName+".items.append('"+itemName+"')")
        #  Add to item table with column & kanban id
        #  Separate kanban item tables, but all columns incl in 1 table

    def removeItem(self, colNum, itemNum):
        print(eval("self." + self.cols[colNum-1] + ".items[" + str(itemNum-1) +
                   "]"))
        del eval("self." + self.cols[colNum-1] + ".items")[itemNum-1]
        #  Remove item from item list

    def moveItem(self, colFrom, itemNum, colTo):
        self.addItem(self.cols[colTo-1], eval("self." + self.cols[colFrom-1] +
                                              ".items[" + str(itemNum-1) +
                                              "]"))
        self.removeItem(colFrom, itemNum)
        self.list()
        #  Change db foreign key (column id)

    def __exit__(self, exc_type, exc_value, traceback):
        print('Goodbye')


def main():
    seed.main()
    #  Display kanban & list items
    kan = Kanban()
    print(kan.table)
    # kan.list()


if __name__ == "__main__":
    main()
