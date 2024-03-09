'''
Question's too long
'''

number = int(input())
station_dict = {}
for i in range(number):
    name = input()
    station_dict[name] = {}
    numberComp = int(input())
    for i in range(numberComp):
        detail = input().split(",")
        station_dict[name][detail[0]] = int(detail[1])
