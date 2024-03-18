'''
Question's too long
'''

def count(L, word):
    if not L:
        return 0
    else:
        if L[0] == word:
            return 1 + count(L[1:], word)
        else:
            return count(L[1:], word)
