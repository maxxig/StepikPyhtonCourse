import math

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
def mysort(val):
    return math.sqrt(val[0]**2 + val[1]**2)
points=sorted(points, key=mysort)
print(points)