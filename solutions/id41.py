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

from itertools import permutations

def largest_pandigital_prime():
    for n in range(9, 0, -1):
        pandigitals = permutations(range(1, n + 1))
        for p in sorted(pandigitals, reverse=True):
            num = int(''.join(map(str, p)))
            if is_prime(num):
                return num

print(largest_pandigital_prime())