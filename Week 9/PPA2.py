'''
Write a function named read_line that accepts a text file named filename and a positive integer n as arguments.
Within the function, read the file and return the nth line of the file. If the file has fewer than n lines, return the string 'None'.
'''

def read_line(filename, n):
    s = open(filename, 'r')
    lines = s.readlines()
    if n > len(lines):
        return 'None'
    return lines[n-1]
