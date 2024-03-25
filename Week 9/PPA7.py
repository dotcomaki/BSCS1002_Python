'''
filename points to the name of some text file. Each line in this file is missing a period at the end of the line.
Write a function named add_period that accepts filename as argument and creates a new file named out.txt.
The function should copy the contents of filename into out.txt and add a period at the end of each line.
'''


def add_period(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    file = open('out.txt', 'w')
    for line in lines:
        file.write(line.rstrip() + '.\n')
    file.close()
    return None
