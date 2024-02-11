'''
Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.
'''

L = input().split(',')
L.reverse()

for i in range(len(L)):
    if i != len(L) - 1:
        print(L[i], end=',')
    else:
        print(L[i])
