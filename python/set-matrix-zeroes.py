class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(a)
        c = len(a[0])
        firstRow = False
        firstCol = False
        for i in range(r):
            for j in range(c):
                if (a[i][j] == 0):
                    if (i == 0):
                        firstRow = True
                    if (j == 0):
                        firstCol = True
                    a[0][j] = 0
                    a[i][0] = 0
        # print(a)
        for i in range(1, r):
            for j in range(1, c):
                if (a[0][j] == 0 or a[i][0] == 0):
                    a[i][j] = 0
        # print(firstRow, firstCol)
        if (firstCol == True):
            for i in range(r):
                a[i][0] = 0
        if (firstRow == True):
            for j in range(c):
                a[0][j] = 0

        return a
