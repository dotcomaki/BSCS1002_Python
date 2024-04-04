'''
Write a function named to_dict that accepts a list of tuples as argument. Each tuple will be a collection of integers. Create a dictionary whose keys are these tuples. The value corresponding to a key is the sum of squares of the integers in the tuple. Use dictionary comprehension and built-in functions.
'''

def to_dict(t):
    return {i: sum(map(lambda x: x**2, i)) for i in t}
