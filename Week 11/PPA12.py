'''
Write a function named extract_keys that accepts a dictionay as argument and returns the list of keys that satisfy the following condition: the key is less than 50 and the corresponding value is greater than 100. The list returned should be sorted in descending order. The keys and values are both integers. Use list comprehension and built-in functions.
'''

def extract_keys(d):
    return sorted([k for k,v in d.items() if k < 50 and v > 100], reverse=True)
