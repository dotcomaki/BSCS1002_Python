'''
Question's too long
'''

def number_grid(m, n):
    file = open('numgrid.csv', 'w')
    number = 1
    for i in range(m):
        for j in range(n):
            file.write(str(number))
            if j != n - 1:
                file.write(',')
            number += 1
        file.write('\n')
    file.close()
