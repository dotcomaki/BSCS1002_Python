'''
Write a recursive function named factorial that accepts a positive integer n as argument and returns the factorial of n.
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
