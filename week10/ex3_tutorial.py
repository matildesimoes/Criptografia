def mod11(n):
    return n % 11

def compute_points():
    points = []
    for x in range(11):
        for y in range(11):
            if mod11(y ** 2) == mod11(x ** 3 + x + 6):
                points.append((x, y))
    return points

points = compute_points()
for point in points:
    print(point)
