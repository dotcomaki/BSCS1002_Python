'''
Write a function named get_range that accepts a list of real numbers as argument. It should return the range of the list.
'''

min = max = None
def get_range(L):
    minim = L[0]
    maxim = L[0]
    ran = 0.0
    for i in range(len(L)):
        if L[i] > maxim:
            maxim = L[i]
        if L[i] < minim:
            minim = L[i]

    ran = maxim - minim
    return ran
