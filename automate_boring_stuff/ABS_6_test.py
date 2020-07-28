tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'gooooooooose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    print(colWidths)

printTable()


def printTable2():
    colWidths = [0,""] * len(tableData)
    print(colWidths)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[2*i]:
                colWidths[2*i] = len(tableData[i][j])
                colWidths[2*i+1] = tableData[i][j]
    print(colWidths)

printTable2()

