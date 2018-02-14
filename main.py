import seed
import math
from db import Db


class Kanban():

    def load(self):
        data = Db.read()
        self.parse(data)

    def printOut(self):
        self.load()
        out = '\n'
        maxRow = min(10, max([len(col[1]) for col in self.table]))
        maxRow = 0

        for col in self.table:
            padd = max(0, (19-col[0].__len__())/2)
            out += math.floor(padd)*' ' + col[0] + math.ceil(padd)*' '
            numItems = len(col[1])
            maxRow = numItems if numItems > maxRow else maxRow

        out += '\n'

        for i in range(0, min(10, maxRow)):
            out = out + '\n'
            for col in self.table:
                if(i < len(col[1])):
                    padd = max(0, (19-col[1][i].__len__())/2)
                    out += math.floor(padd)*' ' + col[1][i][0:19]\
                        + math.ceil(padd)*' '
                else:
                    out += 19*' '

        out += '\n'
        # print(out)
        return out

    def parse(self, data):
        #  Parse data from db into object
        # print('Parsing\n')
        self.table = []
        self.kanId = data[0][0][0]
        self.name = data[0][0][1]

        for col in data[1]:
            self.table.append((col[2], []))

        for item in data[2]:
            self.table[item[2]-1][1].append(item[3])

    def addItem(self, colNum, todo):
        #  Tell Db to append todo to end of specified column
        Db.addItem(colNum, todo)

    def removeItem(self, colNum, rowNum):
        #  Deleting item based on colNum and rowNum as displayed onscreen
        Db.deleteItem(colNum, rowNum)

    def advItem(self, colNum, rowNum):
        #  Advance an item to the next column
        Db.moveItem(colNum, rowNum, colNum+1)
        print("advancing...")


def main():
    # seed.main()
    #  Display kanban & list items
    kan = Kanban()
    print(kan.printOut())

    # for i in range(0,20):
    #     kan.addItem(2, 'Test')
    # kan.addItem(2, 'Test Again')
    # kan.addItem(4, 'Test Again Again')
    # kan.removeItem(4, 1)
    # kan.printOut()


if __name__ == "__main__":
    main()
