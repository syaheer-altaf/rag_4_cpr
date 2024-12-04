def last_ten_digits_of_large_prime():
    base = 2
    exp = 7830457
    multiplier = 28433
    mod = 10**10
    result = pow(base, exp, mod) * multiplier % mod
    result = (result + 1) % mod
    return result

print(last_ten_digits_of_large_prime())