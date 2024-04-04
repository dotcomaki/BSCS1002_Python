'''
Write a function named planar_count that accepts positive integers n, p as arguments. It should return the number of points in the plane with integer coordinates (x, y) such that 0 <= x, y <= n and x * y = p. Use list comprehension.
'''

# Write your code here
def planar_count(n, p):
    return len([(x, y) for x in range(n+1) for y in range(n+1) if x*y == p])
