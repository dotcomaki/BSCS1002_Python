'''
Series Question
'''

n = int(input())
innersum = 0
outersum = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        innersum += j
    outersum += innersum
    innersum = 0
print(outersum)
