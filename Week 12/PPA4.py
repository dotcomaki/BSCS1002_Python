'''
Question's too long
'''

import math

def std_dev(X):
    n = len(X)
    mean = sum(X) / n
    sum_of_squares = sum([(x - mean) ** 2 for x in X])
    return (math.sqrt(sum_of_squares / (n - 1)))

X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}')
