'''
Write a function named is_prime that accepts a positive integer as argument and returns True if it is prime and False otherwise. Use list comprehension and built-in functions.
'''

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
