def sieve_totient(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for multiple in range(p, limit + 1, p):
                phi[multiple] *= (p - 1)
                phi[multiple] //= p
    return phi

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def find_min_ratio(limit):
    phi = sieve_totient(limit)
    min_ratio = float('inf')
    result = 0
    for n in range(2, limit):
        if is_permutation(n, phi[n]):
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                result = n
    return result

print(find_min_ratio(10**7))