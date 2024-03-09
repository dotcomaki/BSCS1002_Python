'''
Question's too long
'''

def matrix_type(M):
    n = len(M)
    diagonal = True
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0:
                diagonal = False
                break
    if not diagonal:
        return 'non-diagonal'
    scalar = True
    for i in range(n):
        if M[i][i] != M[0][0]:
            scalar = False
            break
    if not scalar:
        return 'diagonal'
    identity = M[0][0] == 1
    if not identity:
        return 'scalar'
    return 'identity'
