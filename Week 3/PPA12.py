'''
Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. Print this new string as output. You can assume that all input strings will be in lower case.
'''

first_string = input().lower()
second_string = input().lower()

result_string = ""

for char in second_string:
    if char not in first_string:
        result_string += char

print(result_string)
