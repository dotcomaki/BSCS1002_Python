'''
Write a function named identity_matrix that accepts a positive integer n as argument and returns an identity matrix of shape n x n. Use list comprehension.
'''

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
