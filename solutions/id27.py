def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(a, b):
    n = 0
    while True:
        value = n * n + a * n + b
        if value <= 0 or not is_prime(value):
            break
        n += 1
    return n

def find_quadratic_coefficients(limit):
    max_primes = 0
    best_a = 0
    best_b = 0
    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            primes = count_primes(a, b)
            if primes > max_primes:
                max_primes = primes
                best_a = a
                best_b = b
    return best_a, best_b

best_a, best_b = find_quadratic_coefficients(1000)
result = best_a * best_b
print(result)