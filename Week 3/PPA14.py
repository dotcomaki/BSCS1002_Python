'''
Two integers are co-prime if the only common divisor between the two integers is one.
Accept two positive integers as input in two different lines. Print Coprime if the two integers are co-prime, else print Not Coprime. Assume that both the integers are greater than two.
'''

x = int(input())
y = int(input())
sum = 0
for i in range(1, x+1):
    if x % i == 0:
        if y % i == 0:
            sum += 1
if sum == 1:
    print("Coprime")
else:
    print("Not Coprime")
