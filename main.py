class kanban():

    cols = []

    # def __init__(self):
    #     print("Hello")

    def list(self):
        for col in eval("self.cols"):
            print(col)
            for i in range(len(eval("self."+col+".items"))):
                    print("  " + str(i+1) + ": " + eval("self." + col + ".items["+str(i)+"]"))


    def addCol(self, colName):
        exec("self." + colName + "=self.column()")
        self.cols.append(colName)




    def addItem(self, colName, itemName):
        exec("self."+colName+".items.append('"+itemName+"')")


    class column():

        def __init__(self):
            self.items = []

        # def addItem(self, itemName)

    # def list(self):
    # def addItem(self):
    # def moveItem(self):
    # def addColumn(self):
    #
# class column(kanban):
#     # def __init__(self):
#     #     print('Hello World!')
#     val2=0
#
#     def test(self):
#         print("World")
#


def main():
    kan=kanban()
    kan.addCol("ToDo")
    kan.addCol("Next")
    kan.addItem("ToDo","Jump")

    kan.list()



if __name__=="__main__":
    main()

