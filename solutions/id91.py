def is_right_triangle(x1, y1, x2, y2):
    a = x1**2 + y1**2
    b = x2**2 + y2**2
    c = (x2 - x1)**2 + (y2 - y1)**2
    return (a + b == c) or (b + c == a) or (c + a == b)

LIMIT = 51
right_triangle_count = 0

for x1 in range(LIMIT):
    for y1 in range(LIMIT):
        for x2 in range(LIMIT):
            for y2 in range(LIMIT):
                if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2):
                    right_triangle_count += 1

print(right_triangle_count)