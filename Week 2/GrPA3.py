'''
Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output.
Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.
'''

string = input()
string = string.lower()
vowels = ''

if 'a' in string:
    vowels += 'a'
if 'e' in string:
    vowels += 'e'
if 'i' in string:
    vowels += 'i'
if 'o' in string:
    vowels += 'o'
if 'u' in string:
    vowels += 'u'

if(vowels == ''):
    print('none')
else:
    print(vowels)
