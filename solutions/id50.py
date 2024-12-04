def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    primes = [i for i in range(2, limit + 1) if sieve[i]]
    return primes

def longest_sum_of_consecutive_primes(limit):
    primes = prime_sieve(limit)
    prime_set = set(primes)
    max_length = 0
    prime_with_max_sum = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum > limit:
                break
            if prime_sum in prime_set:
                max_length = j - i
                prime_with_max_sum = prime_sum

    return prime_with_max_sum

result = longest_sum_of_consecutive_primes(1000000)
print(result)