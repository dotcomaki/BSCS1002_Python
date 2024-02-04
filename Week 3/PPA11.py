'''
Question's too long
'''

n = int(input())
found_solution = False

for x in range(1, n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            if x*x + y*y == z*z:
                print(x, y, z, sep = ',')
                found_solution = True

if not found_solution:
    print("NO SOLUTION")
