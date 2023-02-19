def distance_between_points(a, b):
    sqrt = ((a[0] - b[0])**2)+((a[1] - b[1])**2)
    d = round(sqrt ** 0.5, 6)
    return d
x = 3, 5
y = 3, 3

print(distance_between_points(Point(3, 3), Point(3, 3)))