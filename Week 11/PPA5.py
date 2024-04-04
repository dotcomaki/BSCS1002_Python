'''
Write a function named sort_dict that accepts a dictionary as argument. Convert the dictionary into a list of tuples (key, value pairs), sort this based on the values, and return this list. Use built-in functions. Assume that no two values in the dictionary are the same.
'''

def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1])
