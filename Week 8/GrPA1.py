'''
Write a recursive function named reverse that accepts a list L as argument and returns the reversed list.
'''

def reverse(L):
    if len(L) == 0:
        return []
    else:
        return [L[-1]] + reverse(L[:-1])
