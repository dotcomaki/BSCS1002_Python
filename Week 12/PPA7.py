'''
A clockwise rotation of a list consists of taking the last element and moving it to the beginning of the list.
For instance, if we rotate the list [1, 2, 3, 4, 5], we get [5, 1, 2, 3, 4]. If we rotate it again, we get [4, 5, 1, 2, 3]. Your task is to perform k rotations of a list.
The first line of input contains a non-empty sequence of comma-separated integers. The second line of input is a positive integer k.
Perform k rotations of the list and print it as a sequence of comma-separated integers.
'''

lst = list(map(int, input().split(',')) )
k = int(input())

for i in range(k):
    lst = [lst[-1]] + lst[:-1]
    
print(','.join(map(str, lst)))
