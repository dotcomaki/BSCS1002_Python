'''
Question's too long
'''

def merge(D1,D2,priority):
    D = {}
    for i in D1:
        D[i] = D1[i]
    if (priority == 'first'):
        for i in D2:
            if i not in D:
                D[i] = D2[i]
    elif (priority == 'second'):
        for i in D2:
            D[i] = D2[i]
    print(D)
