import math

def count_fractions_in_range(limit, lower, upper):
    count = 0
    for d in range(2, limit + 1):
        for n in range(math.ceil(d * lower), math.floor(d * upper) + 1):
            if math.gcd(n, d) == 1:
                count += 1
    return count

print(count_fractions_in_range(12000, 1/3, 1/2))