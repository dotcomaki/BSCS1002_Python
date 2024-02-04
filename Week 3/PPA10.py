'''
Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n], endpoints inclusive. If there are no prime numbers in the given range, then print 0.
'''

def isPrime(num):
    count = 0
    for i in range(1, n + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0

n = int(input())
sum = 0
for j in range(1, n + 1):
     if isPrime(j) == 1:
        sum += j
print(sum)
