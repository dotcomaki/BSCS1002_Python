'''
Question's too long
'''

def rotate(mat):
    final = []
    row = len(mat)
    col = len(mat[0])
    for i in range(col):
        x = []
        for j in range(row):
            x.append(mat[row-1-j][i])
        final.append(x)
        x = []
    return final
