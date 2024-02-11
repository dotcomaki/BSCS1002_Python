'''
Accept a sequence of words as input, append all these words to a list in the order in which they are entered, and print this list as output.
The first line in the input is a positive integer n that denotes the number of words in the sequence. The next n lines will have one word on each line.
'''

n = int(input())
l = []
for i in range(n):
    str = input()
    l.append(str)
print(l)
