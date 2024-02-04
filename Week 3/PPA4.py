'''
Accept a positive integer n as input, where n>1. Print PRIME if n is a prime number and NOTPRIME otherwise.
'''

n = int(input())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("PRIME")
else:
    print("NOTPRIME")
