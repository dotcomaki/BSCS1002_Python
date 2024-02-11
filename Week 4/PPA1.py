'''
Accept a positive integer n as input and print the list of first n positive integers as output.
'''

n = int(input())
l = []
for i in range(n):
    l.append(i+1)
print(l)
