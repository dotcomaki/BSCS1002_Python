'''
Question's too long
'''

def power(A, m):
    if m == 1:
        return A
    else:
        B = power(A, m-1)
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A)):
                sum = 0
                for k in range(len(A)):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            result.append(row)
        return result
