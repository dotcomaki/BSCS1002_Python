'''
Write a function named mat_mul that accepts two matrices of compatible dimensions and returns their matrix product. Use list comprehension and built-in functions.
'''

def mat_mul(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        result.append(row)
    return result
