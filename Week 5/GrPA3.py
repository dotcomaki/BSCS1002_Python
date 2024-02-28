'''
Write a function named distance that accepts two words as arguments and returns the distance between them.
'''

def distance(word_1, word_2):
    if len(word_1) != len(word_2):
        return -1
    elif len(word_1) == len(word_2):
        sum = 0
        for i in range(len(word_1)):
            if ord(word_1[i]) > ord(word_2[i]):
                sum += (ord(word_1[i]) - ord(word_2[i]))
            else:
                sum += (ord(word_2[i]) - ord(word_1[i]))
        return sum
