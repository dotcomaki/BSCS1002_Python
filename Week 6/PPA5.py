'''
Write the following functions:
(1) dict_to_list: accept a dictionary D as argument. Return the key-value pairs in D as a list L of tuples. That is, every element of L should be of the form (key, value) such that D[key] = value.
Going the other way, every key-value pair in the dictionary should be present as a tuple in the list L.
(2) list_to_dict: accept a list of tuples L as argument. Each element of L is of the form (x, y). Return a dict D such that each tuple (x, y) corresponds to a key-value pair in D. That is, D[x] = y.
'''

def dict_to_list(D):
    L = []
    for key in D:
        L.append((key, D[key]))
    return L


def list_to_dict(L):
    D = {}
    for x, y in L:
        D[x] = y
    return D
