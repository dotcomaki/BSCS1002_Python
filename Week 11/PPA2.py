'''
Write a function named is_perfect that accepts a positive integer as argument and returns True if it is a perfect number and False otherwise. Use list comprehension and built-in functions.
'''

def is_perfect(n):
    return n == sum([i for i in range(1, n) if n % i == 0])
