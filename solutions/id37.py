def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n)-i])):
            return False
    return True

def find_truncatable_primes(limit):
    truncatable_primes = []
    for n in range(10, limit):
        if is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes
result = find_truncatable_primes(1000000)
print(sum(result))