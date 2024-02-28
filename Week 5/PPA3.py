'''
Write a function maxval that accepts three integers a, b and c as arguments. It should return the maximum among the three numbers.
'''

def maxval(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
