from math import log10, sqrt

M = 1000000000
sqrt5 = sqrt(5)
phi = log10((sqrt5 + 1) / 2)
logsqrt5 = log10(sqrt5)

def is_pandigital(n):
    if n < 100000000: return False
    flags = [0] * 10
    flags[0] = 1
    while n > 0:
        n, m = n // 10, n % 10
        if flags[m]: return False
        flags[m] = 1
    return True

def get_first_digits(n, s):
    return n // (10 ** (int(log10(n)) - 8))

a, b, k = 1, 1, 2
while True:
    a, b, k = b, a + b, k + 1
    a, b, k = b % M, (a + b) % M, k + 1
    if is_pandigital(b):
        phik = phi * k - logsqrt5
        n = int(10 ** (phik - int(phi * k) + 9)) // 10
        if is_pandigital(n): break

print(k)