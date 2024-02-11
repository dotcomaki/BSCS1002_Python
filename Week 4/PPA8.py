'''

'''

n = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(matrix[i][j], end=',')
        else:
            print(matrix[i][j])
