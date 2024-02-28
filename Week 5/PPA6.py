'''
Write a function named type_of_sequence that accepts a list of words as an argument. Its return value is a string that depends on the number of mysterious words in the sequence.
'''

def type_of_sequence(words):
    count = 0
    for word in words:
        if mysterious(word):
            count += 1

    if count < 2:
        return 'mildly mysterious'
    elif 2 <= count < 5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'
