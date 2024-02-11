'''
In the first line of input, accept a sequence of space-separated words. In the second line of input, accept a single word. If this word is not present in the sequence, print NO.
If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.
'''

seq = input()
L = seq.split(' ')
word = input()

count = 0
for i in range(len(L)):
    if L[i] == word:
        count += 1
        
if count > 0:
    print('YES')
    print(count)
else:
    print("NO")
