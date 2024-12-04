import math

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def find_consecutive_numbers_with_four_prime_factors():
    n = 2
    consecutive_count = 0
    while True:
        if len(prime_factors(n)) == 4:
            consecutive_count += 1
            if consecutive_count == 4:
                return n - 3
        else:
            consecutive_count = 0
        n += 1

result = find_consecutive_numbers_with_four_prime_factors()
print(result)