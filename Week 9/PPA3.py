'''
Write a function named get_max_line that accepts a text file named filename as argument. Each line in this file contains an integer.
The function should return the line number that houses the maximum integer in the file. If multiple lines have the same maximum number, return the smaller of the two.
Line numbers start from one and not zero.
'''

def get_max_line(filename):
    s = open(filename, 'r')
    lines = s.readlines()
    max_num = -1
    max_line = -1
    line_number = 1
    for line in lines:
        num = int(line.strip())
        if num > max_num:
            max_num = num
            max_line = line_number
        line_number += 1
    return max_line
