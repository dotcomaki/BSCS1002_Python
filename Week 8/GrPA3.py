'''
Write a recursive function named collatz that accepts a positive integer n as argument, where 1<n≤32,000, and returns the number of times f has to be applied repeatedly in order to first reach 1.
'''

def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz(n//2)
    else:
        return 1 + collatz(3*n+1)
