'''
A data entry operator has a faulty keyboard. The keys 0 and 1 are very unreliable. Sometimes they work, sometimes they don't. While entering phone numbers into a database,
the operator uses the letter 'l' as a replacement for 1 and 'o' as a replacement for 0 whenever these binary digits let him down. Both 'l' and 'o' are in lower case. 'l' is the first letter of the word 'land', and not capital 'i'.
Accept a ten-digit number as input. Find the number of places where the numbers 0 and 1 have been replaced by letters. If there are no such replacements, print the string No mistakes.
If not, print the number of mistakes (replacements) and in the next line, print the correct phone number.
'''

number = input()
mistakes = 0
correct = ''
for i in range(len(number)):
    if number[i] == 'l':
        mistakes += 1
        correct += '1'
    elif number[i] == 'o':
        mistakes += 1
        correct += '0'
    else:
        correct += number[i]
if mistakes == 0:
    print('No mistakes')
else:
    print(mistakes, "mistakes")
    print(correct)
