'''
filename is a text file that contains a collection of words in lower case, one word on each line. Write a function named get_freq that accepts filename as argument.
It should return a dictionary where the keys are distinct words in the file, the values are the frequencies of these words in the file.
For example, given the following file:
good
great
good
work
work
The dictionary returned should be:
{'good': 2, 'great': 1, 'work': 2}
The order in which the words are added to the dictionary doesn't matter.
'''

def get_freq(filename):
    f = open (filename, 'r')
    words = f.read().splitlines()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
