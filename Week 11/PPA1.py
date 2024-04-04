'''
Write a function named factors that accepts a positive integer as input and returns a list of factors of the number in ascending order. Use list comprehension
'''

def factors(n):
    return [i for i in range(1, n+1) if n % i == 0]
