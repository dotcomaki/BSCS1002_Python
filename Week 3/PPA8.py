'''
Accept a positive integer n as input and print the first n integers on a line separated by a comma.
'''

n = int(input())
for i in range(1, n+1):
    if i < n:
        print(i, end=",")
    else:
        print(i) 
