def pythagorean_triplet_count(limit):
    count = [0] * (limit + 1)
    for m in range(2, int((limit // 2) ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                perimeter = a + b + c
                while perimeter <= limit:
                    count[perimeter] += 1
                    perimeter += a + b + c
    return sum(1 for x in count if x == 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(pythagorean_triplet_count(1500000))