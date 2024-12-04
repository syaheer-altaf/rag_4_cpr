def is_prime(n, sieve):
    if n < 2:
        return False
    return sieve[n]

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n, sieve):
    for rotation in rotations(n):
        if not is_prime(rotation, sieve):
            return False
    return True

def count_circular_primes(limit):
    sieve = generate_primes(limit)
    count = 0
    for i in range(2, limit):
        if is_circular_prime(i, sieve):
            count += 1
    return count

result = count_circular_primes(1000000)
print(result)