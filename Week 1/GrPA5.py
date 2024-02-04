'''
Accept two positive integers x and y as input. Print the number of digits in x^y.
'''

x = int(input())
y = int(input())
power = x ** y
countPower = str(power)
print(len(countPower))
