'''
Question's too long
'''

def poly(L, x_0):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + x_0 * poly(L[1:], x_0)
