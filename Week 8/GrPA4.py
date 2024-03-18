'''
Write a recursive function named steps that accepts a positive integer n as argument. It should return the total number of ways in which Fibonacci can ascend n steps. Note that the order of his steps is important.
'''

def steps(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        return steps(n-1)+steps(n-2)+steps(n-3)
