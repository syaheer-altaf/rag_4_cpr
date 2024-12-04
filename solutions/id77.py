def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def count_prime_sums(limit):
    primes = generate_primes(limit)
    ways = [0] * (limit + 1)
    ways[0] = 1
    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]
    return ways

limit = 10
while True:
    ways = count_prime_sums(limit)
    if ways[limit] > 5000:
        print(limit)
        break
    limit += 1