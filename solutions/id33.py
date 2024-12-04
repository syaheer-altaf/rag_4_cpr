from math import gcd

def is_curious_fraction(n, d):
    str_n, str_d = str(n), str(d)
    common_digits = set(str_n) & set(str_d)
    if '0' in common_digits: 
        return False
    for digit in common_digits:
        new_n = int(str_n.replace(digit, '', 1))
        new_d = int(str_d.replace(digit, '', 1))
        if new_d != 0 and n * new_d == d * new_n:
            return True
    return False

def product_of_curious_fractions():
    product_numerator = 1
    product_denominator = 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if is_curious_fraction(numerator, denominator):
                product_numerator *= numerator
                product_denominator *= denominator
    common_divisor = gcd(product_numerator, product_denominator)
    return product_denominator // common_divisor

result = product_of_curious_fractions()
print(result)