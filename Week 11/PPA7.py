'''
Write a function named all_even that accepts a list of integers as arguments and returns True if all entries of the list are even and False otherwise. Use list comprehension and built-in functions.
'''

def all_even(lst):
    return all([x % 2 == 0 for x in lst])
