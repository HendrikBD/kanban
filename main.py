import seed
import db


class Kanban():

    cols = []
    kanbanId = 0

    def __init__(self):
        self.parse(db.load('ToDo'))
        print('hello?')
        #  Load column categories from db function

    def list(self):
        for col in eval("self.cols"):
            print(col)
            for i in range(len(eval("self."+col+".items"))):
                    print("  " + str(i+1) + ": " + eval("self." + col +
                                                        ".items["+str(i)+"]"))
            #  List, optimized for terminal/general purpose

    def parse(self, data):
        print('Parsing')

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

    class column():

        colId = 0

        def __init__(self):
            self.items = []
            #  Load items from db
            #  add item as method


def main():
    #  Seed db suggested structure (first drop, then seed new data)
    #  Display kanban & list items
    kan = Kanban()
    kan.list()


if __name__ == "__main__":
    main()
