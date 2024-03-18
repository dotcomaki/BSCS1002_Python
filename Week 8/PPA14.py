'''
Write a recursive function named det that accepts a square matrix as argument and returns its determinant. In the process of writing this function, it would be useful to look into GrPA-3 of week-7.
A good approach would be to write two functions: det and minor_matrix.
'''

def minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += ((-1)**i) * matrix[0][i] * det(minor_matrix(matrix, 0, i))
        return determinant
