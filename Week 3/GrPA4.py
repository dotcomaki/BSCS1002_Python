'''
Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
'''

def sortString(str):
    str = ''.join(sorted(str))
    print(str)

s = input().lower()
sortString(s)
