def triangle(n):
    return n * (n + 1) // 2

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def is_hexagonal(x):
    n = (1 + (1 + 8 * x) ** 0.5) / 4
    return n.is_integer()

def find_next_triangle():
    n = 286
    while True:
        t = triangle(n)
        if is_pentagonal(t) and is_hexagonal(t):
            return t
        n += 1

result = find_next_triangle()
print(result)