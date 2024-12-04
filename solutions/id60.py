def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def can_concat(p1, p2):
    return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))

primes = []
for i in range(2, 10000):
    if is_prime(i):
        primes.append(i)

def find_set_of_primes(primes):
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if can_concat(primes[i], primes[j]):
                for k in range(j + 1, len(primes)):
                    if can_concat(primes[i], primes[k]) and can_concat(primes[j], primes[k]):
                        for l in range(k + 1, len(primes)):
                            if can_concat(primes[i], primes[l]) and can_concat(primes[j], primes[l]) and can_concat(primes[k], primes[l]):
                                for m in range(l + 1, len(primes)):
                                    if can_concat(primes[i], primes[m]) and can_concat(primes[j], primes[m]) and can_concat(primes[k], primes[m]) and can_concat(primes[l], primes[m]):
                                        return [primes[i], primes[j], primes[k], primes[l], primes[m]]

result_set = find_set_of_primes(primes)
sum_of_primes = sum(result_set)
print(f"Lowest sum of five primes: {sum_of_primes}")