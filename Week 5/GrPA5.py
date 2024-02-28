'''
Write a function named transpose that accepts a matrix mat as input and returns its transpose.
'''

def transpose(mat):
    col = len(mat)
    row = len(mat[0])
    matTrans = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(col):
        for j in range(row):
            matTrans[j][i] = mat[i][j]

    return matTrans
