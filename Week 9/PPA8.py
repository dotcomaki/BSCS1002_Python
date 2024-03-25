'''
The scores of a class of students in the online degree program is represented as a CSV file with the following header:
Name,Gender,CT,Python,PDSA
The name of the file is given by the variable filename. The first line will be the header.
Write a function named improvement which accepts the filename as argument. It should return the number of students whose scores have increased across the three courses.
That is, the number of students whose scores are in this order: CT < Python < PDSA.
'''


def improvement(filename):
    f = open(filename, 'r')
    data = f.readlines()[1:]
    count = 0
    for line in data:
        line = line.strip().split(',')
        if int(line[2]) < int(line[3]) < int(line[4]):
            count += 1
    return count
