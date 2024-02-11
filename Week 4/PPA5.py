'''
Accept a space-separated sequence of positive real numbers as input. Convert each element of the sequence into the greatest integer less than or equal to it. Print this sequence of integers as output, with a comma between consecutive integers.
'''

seq = input().split(' ')
for i in range(len(seq)):
    seq[i] = float(seq[i])
    seq[i] = int(seq[i])

for i in range(len(seq)):
    if i != len(seq) - 1:
        print(seq[i], end=',')
    else:
        print(seq[i])
