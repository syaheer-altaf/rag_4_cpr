def euler_totient(limit):
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i
    return phi

def count_fractions(limit):
    phi = euler_totient(limit)
    return sum(phi) - 1

print(count_fractions(1000000))