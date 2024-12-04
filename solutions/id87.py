def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = 50000000
primes = [p for p in range(2, int(limit ** 0.5) + 1) if is_prime(p)]

prime_squares = [p ** 2 for p in primes if p ** 2 < limit]
prime_cubes = [p ** 3 for p in primes if p ** 3 < limit]
prime_fourths = [p ** 4 for p in primes if p ** 4 < limit]

result = set()

for square in prime_squares:
    for cube in prime_cubes:
        for fourth in prime_fourths:
            num = square + cube + fourth
            if num < limit:
                result.add(num)

print(len(result))