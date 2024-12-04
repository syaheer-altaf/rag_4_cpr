def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_curious_number(n):
    return n == sum(factorial(int(digit)) for digit in str(n))

def sum_of_curious_numbers():
    limit = 7 * factorial(9)
    return sum(n for n in range(10, limit) if is_curious_number(n))

result = sum_of_curious_numbers()
print(result)