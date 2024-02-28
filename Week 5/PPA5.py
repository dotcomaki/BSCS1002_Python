'''
Write a function named first_three that accepts a list L of distinct integers as argument. It should return the first maximum, second maximum and third maximum in the list, in this order. You can assume that the input list will have a size of at least three. 
'''

def first_three(L):
    max = L[0]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]

    L.remove(max)
    secMax = L[0]
    for i in range(len(L)):
        if L[i] > secMax:
            secMax = L[i]

    L.remove(secMax)
    thirdMax = L[0]
    for i in range(len(L)):
        if L[i] > thirdMax:
            thirdMax = L[i]

    return(max, secMax, thirdMax)
