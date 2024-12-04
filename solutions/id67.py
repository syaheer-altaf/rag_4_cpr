def read_triangle(filename):
    with open(filename) as f:
        triangle = [list(map(int, line.split())) for line in f.readlines()]
    return triangle

def maximum_total(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

triangle = read_triangle("triangle.txt")
print(maximum_total(triangle))