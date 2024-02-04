'''
Accept a string as input, print Integer if the string is an integer, print Float if it a float, else print None.
'''

word = input()
if word.isdigit():
    print("Integer")
else:
    word = word.replace('.', '',1)
    if word.isdigit():
        print("Float")
    else:
        print("None")
