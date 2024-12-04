import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(limit):
    result = 1
    for i in range(1, limit + 1):
        result = lcm(result, i)
    return result

result = smallest_multiple(20)
print(result)