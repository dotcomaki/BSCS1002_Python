'''
Write a function named is_perfect that accepts a positive integer n as argument and returns True if it is perfect, and False otherwise.
'''

def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
print(is_perfect(int(input())))
