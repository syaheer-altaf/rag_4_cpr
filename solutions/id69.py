def compute_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def max_n_phi_ratio(limit):
    max_ratio = 0
    max_n = 0
    for n in range(2, limit + 1):
        phi_n = compute_totient(n)
        ratio = n / phi_n
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n
    return max_n

print(max_n_phi_ratio(1000000))