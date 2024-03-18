'''
Write a recursive function named non_decreasing that accepts a non-empty list L of integers as argument and returns True if the elements are sorted in non-decreasing order from left to right, and False otherwise.
'''

def non_decreasing(L):
    if len(L) == 1:
        return True
    else:
        if L[0] <= L[1]:
            return non_decreasing(L[1:])
        else:
            return False
