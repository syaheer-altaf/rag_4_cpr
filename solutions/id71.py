import math

def find_left_fraction(limit, target_numerator, target_denominator):
    target_fraction = target_numerator / target_denominator
    best_numerator = 0
    best_denominator = 1
    min_diff = float('inf')

    for d in range(2, limit + 1):
        n = (target_numerator * d - 1) // target_denominator
        if math.gcd(n, d) == 1:
            diff = target_fraction - (n / d)
            if 0 < diff < min_diff:
                best_numerator = n
                best_denominator = d
                min_diff = diff

    return best_numerator

print(find_left_fraction(1000000, 3, 7))