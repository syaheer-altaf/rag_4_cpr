def read_triangles(file_path):
    with open(file_path, 'r') as file:
        triangles = [
            tuple(map(int, line.strip().split(',')))
            for line in file
        ]
    return triangles

def origin_in_triangle(vertices):
    (x0, y0), (x1, y1), (x2, y2) = vertices
    cross1 = x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y0 - y1)
    cross2 = x0 * y1 - x1 * y0
    cross3 = x1 * y2 - x2 * y1
    cross4 = x2 * y0 - x0 * y2

    return (cross1 > 0 and cross2 > 0 and cross3 > 0 and cross4 > 0) or \
           (cross1 < 0 and cross2 < 0 and cross3 < 0 and cross4 < 0)

def count_triangles_with_origin(file_path):
    triangles = read_triangles(file_path)
    count = 0
    for coords in triangles:
        vertices = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
        if origin_in_triangle(vertices):
            count += 1
    return count


file_path = "triangles.txt"
result = count_triangles_with_origin(file_path)
print(result)