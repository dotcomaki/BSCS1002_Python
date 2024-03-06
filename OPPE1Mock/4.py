'''
Question's too long
'''

stats = dict()

for i in range(4):
    L = input().split(',')
    name = L[0]
    total = 0
    for runs in L[1:]:
        total = total + int(runs)
    stats[name] = total
    
print(stats)
