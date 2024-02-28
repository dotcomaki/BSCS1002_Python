'''
Write a function named is_magic that accepts a square matrix as argument and returns YES if it is a magic-square and NO if it isn't one.
'''

def is_magic(mat):
    n = len(mat)
    if n == 0:
        return "NO"

    sumDiag = 0
    for i in range(n):
        sumDiag += mat[i][i]

    sumSecondDiag = 0
    for i in range(n):
        sumSecondDiag += mat[i][n-1-i]

    if sumDiag != sumSecondDiag:
        return "NO"

    targetSum = sumDiag

    for i in range(n):
        sumRow = 0
        sumCol = 0
        for j in range(n):
            sumRow += mat[i][j]
            sumCol += mat[j][i]

        if sumRow != targetSum or sumCol != targetSum:
            return "NO"

    return "YES"
