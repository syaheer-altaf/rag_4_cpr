def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def sum_of_primes(limit):
    sieve = sieve_of_eratosthenes(limit)
    return sum(i for i in range(limit) if sieve[i])

result = sum_of_primes(2000000)
print(result)