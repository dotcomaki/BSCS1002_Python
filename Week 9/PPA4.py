'''
filename points to a CSV file that has two columns. The first column is the name of a student, the second column is this student's age. The first line of the file will always be the header. A sample file is given below for your reference:
Name,Age
Arti,20
Kalam,60
Atul,25
Krishnan,24
Sahana,20
Write a function named get_dict that accepts the filename as argument and returns a dictionary where the keys are the student names and the values are the corresponding ages of the students.
'''

def get_dict(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    student_dict = {}
    for line in lines[1:]:
        name, age = line.strip().split(',')
        student_dict[name] = int(age)

    return student_dict
