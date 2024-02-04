'''
Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.
'''

word = input()
halfpoint = (len(word)//2) + 1
count = 0
for i in range(halfpoint):
    if word[i] != word[-i - 1]:
        count += 1
if count == 0:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
