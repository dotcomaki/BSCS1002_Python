'''
(1) Write a function named insert that accepts a sorted list L of integers and an integer x as arguments. It should return a sorted list with the element x inserted into the input list at the right place.
(2) Write a recursive function named isort that accepts a non-empty list L of integers as argument. It should return a sorted list in ascending order. isort must make use of insert. This is a popular sorting algorithm and is called insertion sort.
'''

def insert(L, x):
    if len(L) == 0:
        return [x]
    if x < L[0]:
        return [x] + L
    return [L[0]] + insert(L[1:], x)

def isort(L):
    if len(L) == 1:
        return L
    return insert(isort(L[:-1]), L[-1])
