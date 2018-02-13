import seed
import math
from db import Db


class Kanban():

    def load(self):
        data = Db.read()
        self.parse(data)

    def printOut(self):
        self.load()
        out = ''
        maxRow = min(10, max([len(col[1]) for col in self.table]))
        maxRow = 0

        for col in self.table:
            padd = max(0, (19-col[0].__len__())/2)
            out += math.floor(padd)*' ' + col[0] + math.ceil(padd)*' '
            numItems = len(col[1])
            maxRow = numItems if numItems > maxRow else maxRow

        for i in range(0, min(10, maxRow)):
            out = out + '\n'
            for col in self.table:
                if(i < len(col[1])):
                    padd = max(0, (19-col[1][i].__len__())/2)
                    out += math.floor(padd)*' ' + col[1][i][0:19]\
                        + math.ceil(padd)*' '
                else:
                    out += 19*' '
        print(out)

    def parse(self, data):
        print('Parsing\n')
        self.table = []
        self.kanId = data[0][0][0]
        self.name = data[0][0][1]

        for col in data[1]:
            self.table.append((col[2], []))

        for item in data[2]:
            self.table[item[2]-1][1].append(item[3])

    def addCol(self, colName):
        exec("self." + colName + "=self.column()")
        self.cols.append(colName)
        #  Add new category to tables with kanban id

    def addItem(self, colNum, todo):
        Db.addItem(colNum, todo)
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


def main():
    seed.main()
    #  Display kanban & list items
    kan = Kanban()
    kan.printOut()
    for i in range(0,20):
        kan.addItem(2, 'Test')
    kan.addItem(2, 'Test Again')
    kan.addItem(4, 'Test Again Again')
    kan.printOut()


if __name__ == "__main__":
    main()
