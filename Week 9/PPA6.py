'''
Question's too long
'''

def write_AP(a_1, d, n):
    f = open('out.txt', 'w')
    for i in range(n):
        f.write(str(a_1 + i * d) + '\n')
    return None
