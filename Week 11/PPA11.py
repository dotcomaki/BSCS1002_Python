'''
Write a function named filter_values that accepts a list of integers as argument and returns a sub-list of integers in the range [40, 100] (end-points inclusive). Preserve the order in which the elements appear in the original list. Use list comprehension or built-in functions.
'''

def filter_values(lst):
    return [i for i in lst if i >= 40 and i <= 100]
