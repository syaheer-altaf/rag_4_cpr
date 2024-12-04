def count_divisors(n, memo):
    if n in memo:
        return memo[n]
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i * i != n else 1
    memo[n] = count
    return count

def find_triangle_number(divisor_limit):
    memo = {}
    n = 1
    triangle_number = 0
    while True:
        triangle_number = n * (n + 1) // 2
        if n % 2 == 0:
            divisors = count_divisors(n // 2, memo) * count_divisors(n + 1, memo)
        else:
            divisors = count_divisors(n, memo) * count_divisors((n + 1) // 2, memo)
        if divisors > divisor_limit:
            return triangle_number
        n += 1

result = find_triangle_number(500)
print(result)