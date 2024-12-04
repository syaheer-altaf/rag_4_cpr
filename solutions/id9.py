def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value // 3):
        for b in range(a + 1, sum_value // 2):
            c = sum_value - a - b
            if a * a + b * b == c * c:
                return a, b, c
    return None

a, b, c = find_pythagorean_triplet(1000)
result = a * b * c
print(result)