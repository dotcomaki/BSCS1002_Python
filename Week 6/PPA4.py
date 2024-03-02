'''
Write a function named value_to_keys that accepts a dictionary D and a variable named value as arguments
It should return the list of all keys in the dictionary that have value equal to value. If the value is not present in the dictionary, the function should return the empty list.
'''

def value_to_keys(D, value):
    l = []
    for key in D:
        if D[key] == value:
            l.append(key)
    return l
