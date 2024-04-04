'''
Write a function named is_diagonal that accepts a square matrix as argument and returns True if it is a diagonal matrix and False otherwise. Use list comprehension and built-in functions.
'''

def is_diagonal(matrix):
    return all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
