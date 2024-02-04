'''
Accept a positive integer as input and print the sum of the digits in the number.
'''

n = int(input())
digit = 0
sum = 0
while(n != 0):
    digit = n % 10
    sum += digit
    n //= 10
print(sum)
