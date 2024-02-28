'''
Write a recursive function named fibo that accepts a positive integer n as argument and returns the nth Fibonacci number. For this problem, F1 = F2 = 1 are the first two Fibonacci numbers.
'''

def fibo(n):
    first = 1
    second = 1
    nextNum = second
    count = 1
    while count < n-1:
        count += 1
        first, second = second, nextNum
        nextNum = first + second
    return nextNum
