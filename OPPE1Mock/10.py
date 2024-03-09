'''
Question's too long
'''

def get_summary(trans):
    D = []
    for i in trans:
        A = {}
        Cost = 0
        for items in i["Items"]:
            Cost += int(items["Price"])*int(items["Qty"])
        A['Cost'] = Cost
        A['TID'] = i['TID']
        D.append(A)
    return D
