

def ZeroMatrix(m):
    print("in Zero Matrix")
    indices = []
    Nrows = len(m)
    Ncolumns = len(m[0])
    for i in range(Nrows):
        for j in range(Ncolumns):
            if m[i][j]==0:
                indices.append(j+Ncolumns*i)
                print(i,j)
    print(indices)

    for ind in indices:
        i = int(ind / Ncolumns)
        j = int(ind % Ncolumns)
        print(ind,i,j)
        #Set rows to 0
        for ic in range(len(m[i])):
            m[i][ic]=0
        #Set columns to 0
        for ir in range(len(m)):
            m[ir][j]=0
    return m

def eraseRow(m, irow):
    for ic in range(len(m[irow])):
        m[irow][ic] = 0

def eraseCol(m, icol):
    for row in m:
        row[icol] = 0

def ZeroMatrixv2(m):
    print("In Zero Matrix _v2")
    firstRow = -1
    for irow in range(len(m)):
        clearRow = False
        for icol in range(len(m)):
            if m[irow][icol] == 0:
                # Store in the first row what needs to be erased
                if (firstRow < 0):
                    firstRow = irow
                else:
                    # This will tell to erase this row after scanning it
                    clearRow = True
                    # This will set the element in the book keeping row to 0
                    m[firstRow][icol] = 0
        if clearRow:
            eraseRow(m, irow)

    if (firstRow >= 0):
        for icol in range(len(m[firstRow])):
            if m[firstRow][icol] == 0:
                eraseCol(m, icol)
            else:
                m[firstRow][icol] = 0


    return m

def printFormat(m):
    for i in range(len(m)):
        print(m[i])


def main():
    Nrows   = 4
    Ncolumns = 3
    m = [[0 for i in range(Ncolumns)] for j in range(Nrows)]
    m = [[1,2,3,4],[0,1,2,3],[4,6,0,3]]
    printFormat(m)
    printFormat(ZeroMatrix(m))
    print("----")
    m = [[1, 2, 3, 4], [0, 1, 2, 3], [4, 6, 0, 3], [5, 7, 1, 3]]
    printFormat(m)
    printFormat(ZeroMatrix(m))
    print("----")
    m = [[1, 2, 3, 4], [0, 1, 2, 3], [4, 6, 0, 3], [5, 7, 1, 3]]
    printFormat(m)
    printFormat(ZeroMatrixv2(m))
    print("----")
    m = [[1, 2, 3, 4], [7, 1, 2, 3], [4, 6, 9, 3], [5, 7, 1, 3]]
    printFormat(m)
    printFormat(ZeroMatrixv2(m))
if __name__ =="__main__":
    main()