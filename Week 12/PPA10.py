'''
Question's too long
'''

def final(n, moves):
    x, y = 1, 1
    for move in moves:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        if x == n+1:
            x = n
        if y == n+1:
            y = n
    return (x, y)
