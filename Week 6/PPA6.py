'''
Write a function named get_marks that accepts the scores_dataset and a variable named subject as arguments.
It should return the marks scored by all students in subject as a list of tuples. Each element in this list is of the form (Name, Marks).
The order in which the tuples are appended to the list doesn't matter.
'''

def get_marks(scores_dataset, subject):
    l = []
    for dic in scores_dataset:
        marks = (dic['Name'], dic[subject])
        l.append(marks)
    return l
