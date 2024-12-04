def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def sum_even_fibonacci(limit):
    n = 1
    total = 0
    while True:
        fib = fibonacci(n)
        if fib > limit:
            break
        if fib % 2 == 0:
            total += fib
        n += 1
    return total

result = sum_even_fibonacci(4000000)
print(result)