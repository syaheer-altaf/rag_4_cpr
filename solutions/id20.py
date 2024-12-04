def factorial(n, memo):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

def sum_of_digits_in_factorial(n):
    memo = {}
    factorial_result = factorial(n, memo)
    return sum(int(digit) for digit in str(factorial_result))

result = sum_of_digits_in_factorial(100)
print(result)