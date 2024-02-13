'''
Question's too long
'''

import math

n = int(input())
points = []

for i in range(n):
    point = input()
    x_str, y_str = point.split(",")
    points.append((int(x_str), int(y_str)))

P_input = input()
P_x_str, P_y_str = P_input.split(",")
P = (int(P_x_str), int(P_y_str))

nearest_points = []
min_distance = None

for point in points:
    distance = math.sqrt((point[0] - P[0])**2 + (point[1] - P[1])**2)
    if min_distance is None or distance < min_distance:
        min_distance = distance
        nearest_points = [point]
    elif distance == min_distance:
        nearest_points.append(point) 
      
for point in nearest_points:
    print(f"{point[0]},{point[1]}")
