'''
Question's too long
'''

def survival(T):
    for x in range(0, 51):
        for y in range(0, 51):
            if 30 + x**2 + y**2 - 3*x - 4*y <= T:
                return True
    return False
