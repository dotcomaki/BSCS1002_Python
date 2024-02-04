'''
Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
'''

x = input()
first = int(x[0])
second = int(x[2])
third = int(x[4])
fourth = int(x[6])
fifth = int(x[8])
print(first*second*third*fourth*fifth)
