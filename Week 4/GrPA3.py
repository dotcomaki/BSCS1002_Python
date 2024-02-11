'''
Multiply matrices A and B
'''

n = int(input())

A = []
for i in range(n):
    row = []
    for x in input().split(','):
        row.append(int(x))
    A.append(row)

B = []
for i in range(n):
    row = []
    for x in input().split(','):
        row.append(int(x))
    B.append(row)

C = []
for i in range(n):
    row = [ ]
    for j in range(n):
        row.append(0)
    C.append(row)

for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(C[i][j], end=',')
        else:
            print(C[i][j])
