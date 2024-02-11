'''
This question introduces you to the idea of prefix codes. Prefix code is a block of visible code that is already provided to you. You have to type your code below the prefix code. Note that the contents of the prefix cannot be modified.
A list L of words is already given to you as a part of the prefix code. Print the longest word in the list. If there are multiple words with the same maximum length, print the one which appears at the rightmost end of the list.
'''

L = input().split(',')
max = ''
maxLen = 0
for word in L:
    if len(word) >= maxLen:
        maxLen = len(word)
        max = word
print(max)
