'''
Question's too long
'''

def minor_matrix(M,i,j):
    final = []
    for a in range(len(M)):
        if a != i:
            t = []
            for b in range(len(M[a])):
                if b != j:
                    t.append(M[a][b])
            final.append(t)
            t = []
    return final
