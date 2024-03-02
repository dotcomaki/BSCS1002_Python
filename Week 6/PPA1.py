'''
Accept a sequence of words as input. Create a dictionary named freq whose keys are the distinct words in the sequence
The value corresponding to a key (word) should be the frequency of occurrence of the key (word) in the sequence.
'''

sequence = input()
sequence = sequence.split(",")
freq = {}
for word in sequence:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
