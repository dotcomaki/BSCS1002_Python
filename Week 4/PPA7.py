'''
This question introduces you to the idea of suffix codes. Suffix code is a block of visible code that will be executed after whatever code you type. You have to type your code above the suffix code. Note that the contents of the suffix code cannot be modified.
Accept a square matrix as input and store it in a variable named matrix. The first line of input will be, n, the number of rows in the matrix. Each of the next n lines will have a sequence of n space-separated integers.
'''

n = int(input())
matrix = []
for i in range(n):
    row = []
    for num in input().split(' '):
        row.append(int(num))
    matrix.append(row)
