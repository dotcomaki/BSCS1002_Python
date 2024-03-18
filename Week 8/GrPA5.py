'''
Ancestry question
'''

def ancestry(P, present, past):
    if present == past:
        return [present]
    else:
        return [present] + ancestry(P, P[present], past)
