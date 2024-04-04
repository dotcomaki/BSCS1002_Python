'''
Write a function named perfect_square that accepts a list of positive integers as argument and returns True if there is at least one perfect square in the list and False otherwise. Use list comprehension and built-in functions.
'''

def perfect_square(lst):
    return any([i**0.5 == int(i**0.5) for i in lst])
