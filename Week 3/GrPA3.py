'''
Question's too long
'''

from math import *
x = 0
y = 0
userInput = ''

while(userInput != 'STOP'):
    userInput = input().upper()
    if userInput == 'UP':
        y += 1
    elif userInput == 'DOWN':
        y -= 1
    elif userInput == 'RIGHT':
        x += 1
    elif userInput == 'LEFT':
        x -= 1

x = abs(x)
y = abs(y)
print(x+y)
