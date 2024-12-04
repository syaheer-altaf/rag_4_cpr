def largest_prime_factor(n, memo={}):
    if n in memo:
        return memo[n]
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            memo[n] = max(factor, largest_prime_factor(n // factor, memo))
            return memo[n]
        factor += 1
    memo[n] = n
    return n

result = largest_prime_factor(600851475143)
print(result)