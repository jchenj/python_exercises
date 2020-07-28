#! /usr/bin/env python3
# printTable.py - A program that takes a list of lists of strings and
# displays it in a table with each column right-justified.
# Each inner list is displayed in a column, organized from top to bottom,
# with the first inner list at the leftmost column.
# Assumes that all the inner lists contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    print(colWidths)
    
    colWidth = (max(colWidths))
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]+2), end="")
        print('')
       
printTable()
