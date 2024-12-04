def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = 0
total = 1
side_length = 1
current = 1

while True:
    side_length += 2
    for _ in range(4):
        current += side_length - 1
        if is_prime(current):
            primes += 1
    total += 4
    if primes / total < 0.1:
        break

print(side_length)