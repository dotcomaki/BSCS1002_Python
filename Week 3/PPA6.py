'''
Question's too long
'''

n = input()
min = 999999999
minStr = ""
while(n != "abcdefghijklmnopqrstuvwxyz"):
    if len(n) < min:
        min = len(n)
        minStr = n
    n = input()
print(minStr)
