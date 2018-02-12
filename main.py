class Kanban():

    cols = []

    def list(self):
        for col in eval("self.cols"):
            print(col)
            for i in range(len(eval("self."+col+".items"))):
                    print("  " + str(i+1) + ": " + eval("self." + col +
                                                        ".items["+str(i)+"]"))

    def addCol(self, colName):
        exec("self." + colName + "=self.column()")
        self.cols.append(colName)

    def addItem(self, colName, itemName):
        exec("self."+colName+".items.append('"+itemName+"')")

    def removeItem(self, colNum, itemNum):
        print(eval("self." + self.cols[colNum-1] + ".items[" + str(itemNum-1) +
                   "]"))
        del eval("self." + self.cols[colNum-1] + ".items")[itemNum-1]

    def moveItem(self, colFrom, itemNum, colTo):
        self.addItem(self.cols[colTo-1], eval("self." + self.cols[colFrom-1] +
                                              ".items[" + str(itemNum-1) +
                                              "]"))
        self.removeItem(colFrom, itemNum)
        self.list()

    class column():

        def __init__(self):
            self.items = []
    # organize output
    # add as command


def main():
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
