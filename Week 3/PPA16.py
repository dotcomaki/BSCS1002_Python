'''
Question's too long
'''

marks = float(input())
options = float(input())
correctOptions = input()
answers = input()
count = 0.0
flag = True

correctOptions = correctOptions.replace(',', '')
answers = answers.replace(',', '')

for i in range(len(answers)):
    if answers[i] not in correctOptions:
        flag = False
    elif answers[i] in correctOptions:
        count += 1.0

if count > 0.0 and flag:
    finalMarks = count * (marks/len(correctOptions))
    print(finalMarks)
else:
    print(0.0)
