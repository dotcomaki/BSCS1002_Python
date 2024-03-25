'''
Question's too long
'''

def get_matrix(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    matrix = []
    for line in lines:
        row = [int(num) for num in line.strip().split(',')]
        matrix.append(row)
    return matrix
