'''
Question's too long
'''

def spiral_recursive(left, right, n):
    if n == 0:
        return left
    if n == 1:
        return right
    return (spiral_recursive(left, right, n - 1) +
            spiral_recursive(left, right, n - 2)) / 2
    

def spiral_iterative(left, right, n):
    if n == 0:
        return left
    if n == 1:
        return right
    c = 0
    for i in range(n - 1):
        left, right = right, (left + right) / 2
    return right
