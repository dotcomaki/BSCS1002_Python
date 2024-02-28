'''
Write a function insert that accepts a sorted list L of integers and an integer x as input. The function should return a sorted list with the element x inserted at the right place in the input list. The original list should not be disturbed in the process.
'''

def insert(L, x):
    outputList = []
    inserted = False
    for elem in L:
        if (not inserted) and (x < elem):
            inserted = True
            outputList.append(x)
        outputList.append(elem)
    if not inserted:
        outputList.append(x)
    return outputList
