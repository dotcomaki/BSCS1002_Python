'''
Write a function named dim_equal that accepts two matrices A and B as arguments. It should return True if the the dimensions of both matrices are the same, and False otherwise.
'''

def dim_equal(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return True
    else:
        return False
