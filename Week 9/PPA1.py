'''
Write a function named read_file that accepts a text file named filename as argument. Within the function, read the file and print each line of the file on a separate line in the console.\
You shouldn't print any extra characters at the end of a line. There shouldn't be an empty line between any two consecutive lines.
'''

def read_file(filename):
    s = open(filename, 'r')
    for line in s:
        print(line.strip())
