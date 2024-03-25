'''
The scores of a class of students in the online degree program is represented as a CSV file with the following header:
SeqNo,Name,Gender,CT,Python,PDSA
The name of the file is given by the variable filename. The first line will be the header. The contents of the file will be in increasing order of sequence numbers.
Write a function named extract_lines that accepts filename as argument. Within the function, read the file and look for all male students who have scored at least 70 marks in Python.
Copy these lines into a new file named python.csv. The entries in this file should be in the increasing order of sequence numbers. Also, the first line of python.csv should be the header, which is same as the one in filename.
'''

def extract_lines(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    header = lines[0]
    lines = lines[1:]
    python = []
    for line in lines:
        line = line.strip().split(',')
        if line[2] == 'M' and int(line[4]) >= 70:
            python.append(','.join(line))
    file.close()

    file = open('python.csv', 'w')
    file.write(header)
    for line in python:
        file.write(line + '\n')
    file.close()
