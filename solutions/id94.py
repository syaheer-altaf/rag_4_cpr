import math
import itertools

LIMIT = 10**9
total_perimeter = 0

for s in itertools.count(1, 2):
    if s * s > (LIMIT + 1) // 3:
        break
    for t in range(s - 2, 0, -2):
        if math.gcd(s, t) == 1:
            a = s * t
            b = (s * s - t * t) // 2
            c = (s * s + t * t) // 2
            if a * 2 == c - 1:
                p = c * 3 - 1
                if p <= LIMIT:
                    total_perimeter += p
            if a * 2 == c + 1:
                p = c * 3 + 1
                if p <= LIMIT:
                    total_perimeter += p
            if b * 2 == c - 1:
                p = c * 3 - 1
                if p <= LIMIT:
                    total_perimeter += p
            if b * 2 == c + 1:
                p = c * 3 + 1
                if p <= LIMIT:
                    total_perimeter += p

print(total_perimeter)