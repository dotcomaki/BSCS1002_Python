'''
Question's too long
'''

n = int(input())
scores_dataset = []
for i in range(n):
    name = input()
    city = input()
    seqno = int(input())
    mathematics = int(input())
    physics = int(input())
    chemistry = int(input())
    dic = {
        'Name': name,
        'City': city,
        'SeqNo': seqno,
        'Mathematics': mathematics,
        'Physics': physics,
        'Chemistry': chemistry
    }
    scores_dataset.append(dic)
