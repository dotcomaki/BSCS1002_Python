'''
Accept a sequence of words as input. Create a dictionary named real_dict whose keys are the letters of the English alphabet. For each key (letter), the corresponding value should be a list of words that begin with this key (letter).
For any given key, the words should be appended to the corresponding list in the order in which they appear in the sequence. You can assume that all words of the sequence will be in lower case.
'''

import string

seq = input().lower().split(',')
real_dict = {}
for word in seq:
    first_letter = word[0]  
    if first_letter in real_dict:
        real_dict[first_letter].append(word)
    else:
        real_dict[first_letter] = [word]
