'''
Logarithm Recursion
'''

def logarithm(x):
    if x == 1:
        return 0
    return 1 + logarithm(x/2)
