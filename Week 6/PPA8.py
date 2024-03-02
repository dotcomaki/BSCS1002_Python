'''
Write the following functions
(1) factors: accept a positive integer n as argument. Return the set of all factors of n.
(2) common_factors: accept two positive integers a and b as arguments. Return the set of common factors of the two numbers. This function must make use of factors.
(3) factors_upto: accept a positive integer n as argument. Return a dict D, whose keys are integers and values are sets. Each integer in the range [1,n], endpoints inclusive, is a key of D.
The value corresponding to a key, is the set of all factors of key. This function must make use of factors.
'''

def factors(n):
    l = set()
    for i in range(1, n + 1):
        if n % i == 0:
            l.add(i)
    return l


def common_factors(a,b):
    s = set()
    if a > b: max = a
    else: max = b
    for i in range(1, max + 1):
        if a % i == 0 and b % i == 0:
            s.add(i)
    return s

def factors_upto(n):
    D = {}
    for i in range(1, n + 1):
        s = set()
        for j in range(1, i + 1):
            if i % j == 0:
                s.add(j)
        D[i] = s
    return D
