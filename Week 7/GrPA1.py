'''
Question's too long
'''

import operator
ipl_team = {'CSK':0, 'DC':0, 'KKR':0, 'MI':0, 'PK':0, 'RCB':0, 'RR':0, 'SH':0}
for i in range(8):
    match = input()
    li = match.split(',')
    length = len(li)
    ipl_team[li[0]] += (length - 1)
sortedDict = dict(sorted(ipl_team.items(), key=operator.itemgetter(1), reverse=True))
for i in sortedDict:
    print(i + ":" + str(sortedDict[i]))
