'''
Accept a phone number as input. A valid phone number should satisfy the following constraints.
(1) The number should start with one of these digits: 6, 7, 8, 9
(2) The number should be exactly 10 digits long.
(3) No digit should appear more than 7 times in the number.
(4) No digit should appear more than 5 times in a row in the number.
If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.
Print the string valid if the phone number is valid. If not, print the string invalid.
'''

def startDigit(num):
    if num[0] == '6' or num[0] == '7' or num[0] == '8' or num[0] == '9':
        return 1
    else:
        return 0

def countDigit(num):
    if len(num) == 10:
        return 1
    else:
        return 0

def sevenTimes(num):
    count = 0
    for i in range(10):
        for j in range(10):
            if int(num[j]) == i:
                count += 1
        if count > 7:
            return 0
        else:
            count = 0
            pass
    return 1


def fiveTimes(num):
    for i in range(10):
        fiveStr = num[i] * 5
        if fiveStr in num:
            return 0
        else:
            pass
    return 1

number = input()
if startDigit(number) == 1 and countDigit(number) == 1 and sevenTimes(number) == 1 and fiveTimes(number) == 1:
    print("valid")
else:
    print("invalid")
