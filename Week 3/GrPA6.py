'''
Accept a positive integer n as input and print a "number arrow" of size n. For example, n=5 should produce the following output:
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
'''

n = int(input())
for i in range (1,n):
    for j in range(1,i):
        print(str(j)+",",end="")
    print(i)

for i in range(n,0,-1):
    for j in range(1,i):
        print(str(j)+",",end="")
    print(i)
