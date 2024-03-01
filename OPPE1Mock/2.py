'''
A float number is said to have a long tail if the number of digits after the decimal point is more than the number of digits before. For example, 12.3214 has a long tail while the number 123.56 does not.
Write a function named long_tail that accepts a list of float numbers as argument and returns the count of the numbers that have a long tail.
'''

def long_tail(L):
    count = 0
    for x in L:
        stringx = str(x)
        length = len(stringx)
        for i in range(length):
            if stringx[i] == '.':
                index = i
                break
        if (length - index - 1) > index:
            count += 1
    return count
