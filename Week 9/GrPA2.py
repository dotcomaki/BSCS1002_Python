'''
Question's too long
'''

def relation(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    f1.close()
    f2.close()

    lines1 = [line.strip() for line in lines1]
    lines2 = [line.strip() for line in lines2]

    if lines1 == lines2:
        return 'Equal'
    else:
        for line in lines1:
            if line not in lines2:
                return 'No Relation'
        return 'Subset'
