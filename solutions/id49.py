def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_permutations():
    primes = [i for i in range(1000, 10000) if is_prime(i)]
    prime_dict = {}
    for p in primes:
        key = ''.join(sorted(str(p)))
        if key not in prime_dict:
            prime_dict[key] = []
        prime_dict[key].append(p)

    return prime_dict

def find_arithmetic_sequence():
    prime_dict = find_prime_permutations()
    for key, primes in prime_dict.items():
        if len(primes) >= 3:
            primes.sort()
            for i in range(len(primes)):
                for j in range(i + 1, len(primes)):
                    p1, p2 = primes[i], primes[j]
                    diff = p2 - p1
                    p3 = p2 + diff
                    if p3 in primes:
                        if {p1, p2, p3} != {1487, 4817, 8147}:
                            return f"{p1}{p2}{p3}"

result = find_arithmetic_sequence()
print(result)