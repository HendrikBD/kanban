class Kanban():

    cols = []

    def __init__(self):
        print('hello?')
        #  Load list from db to local list

    def list(self):
        for col in eval("self.cols"):
            print(col)
            for i in range(len(eval("self."+col+".items"))):
                    print("  " + str(i+1) + ": " + eval("self." + col +
                                                        ".items["+str(i)+"]"))

    def addCol(self, colName):
        exec("self." + colName + "=self.column()")
        self.cols.append(colName)
        #  Add new category table

    def addItem(self, colName, itemName):
        exec("self."+colName+".items.append('"+itemName+"')")
        #  Add items to db
        #  Should items be referenced relatively? Or should each category have
        #  its own table of a list?

    def removeItem(self, colNum, itemNum):
        print(eval("self." + self.cols[colNum-1] + ".items[" + str(itemNum-1) +
                   "]"))
        del eval("self." + self.cols[colNum-1] + ".items")[itemNum-1]
        #  Remove item from list

    def moveItem(self, colFrom, itemNum, colTo):
        self.addItem(self.cols[colTo-1], eval("self." + self.cols[colFrom-1] +
                                              ".items[" + str(itemNum-1) +
                                              "]"))
        self.removeItem(colFrom, itemNum)
        self.list()
        #  Change db location OR reference table

    class column():

        def __init__(self):
            self.items = []
    # organize output
    # add as command


def main():
    #  Seed db suggested structure
    #  Load kanban & list items
    kan = Kanban()
    kan.addCol("ToDo")
    kan.addCol("Next")
    kan.addItem("ToDo", "Jump")

    kan.list()
    print("")
    kan.moveItem(1, 1, 2)
    # print(kan.ToDo.items)
    # kan.removeItem(1,1)
    # kan.list()


if __name__ == "__main__":
    main()
