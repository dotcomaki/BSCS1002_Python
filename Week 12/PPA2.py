'''
Accept two positive integers a and b as arguments and print a rectangular pattern that has a lines. The first and last line should have b stars,
all other lines should have exactly two stars that are aligned with either end of the rectangle. You can assume that a,b≥2 for all test cases.
'''

def print_rectangle(a, b):
    for i in range(a):
        if i == 0 or i == a - 1:
            print('o' * b)
        else:
            print('o' + ' ' * (b - 2) + 'o')
