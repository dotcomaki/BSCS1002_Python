'''
Accept a positive integer n, with n>1, as input from the user and print all the prime factors of n in ascending order.
'''

def isPrime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0

n = int(input())
for j in range(2, n + 1):
    if n % j == 0 and isPrime(j) == 1:
        print(j)
