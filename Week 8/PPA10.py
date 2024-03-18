'''
Question's too long
'''

def search(L, k):
    if len(L) == 0:
        return False
    else:
        mid = len(L) // 2
        if L[mid] == k:
            return True
        elif L[mid] < k:
            return search(L[mid + 1:], k)
        else:
            return search(L[:mid], k)
