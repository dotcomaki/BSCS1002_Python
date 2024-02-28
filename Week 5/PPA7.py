'''
Question's too long
'''

def is_empty(L):
    if len(L) == 0:
        return True
    else:
        return False

def first(L):
    if len(L) > 0:
        return L[0]
    else:
        return 'None'

def last(L):
    if len(L) > 0:
        return L[-1]
    else:
        return 'None'

def init(L):
    if len(L) > 0:
        return L[0:-1]
    else:
        return 'None'

def rest(L):
    if len(L) > 0:
        return L[1:]
    else:
        return 'None'
