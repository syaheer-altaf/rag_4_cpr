def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_patterns(number):
    str_num = str(number)
    patterns = []
    length = len(str_num)
    for mask in range(1, 1 << length):
        pattern = []
        for i in range(length):
            if mask & (1 << i):
                pattern.append('*')
            else:
                pattern.append(str_num[i])
        patterns.append(''.join(pattern))
    return patterns

def count_primes_in_family(pattern):
    count = 0
    smallest_prime = None
    for digit in '0123456789':
        candidate = int(pattern.replace('*', digit))
        if candidate >= 10 ** (len(pattern) - pattern.count('*')) and is_prime(candidate):
            count += 1
            if smallest_prime is None:
                smallest_prime = candidate
    return count, smallest_prime

def find_smallest_prime_with_family(target_family_size):
    num = 11
    while True:
        if is_prime(num):
            for pattern in generate_patterns(num):
                count, smallest_prime = count_primes_in_family(pattern)
                if count == target_family_size:
                    return smallest_prime
        num += 2

result = find_smallest_prime_with_family(8)
print(result)