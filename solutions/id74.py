import math

def get_chain_length(start_number):
    seen_numbers = set()
    while True:
        seen_numbers.add(start_number)
        start_number = calculate_factorial_sum(start_number)
        if start_number in seen_numbers:
            return len(seen_numbers)

def calculate_factorial_sum(number):
    total = 0
    while number != 0:
        total += factorial_cache[number % 10]
        number //= 10
    return total

factorial_cache = [math.factorial(i) for i in range(10)]
LIMIT = 10**6
result = str(sum(1 for start in range(LIMIT) if get_chain_length(start) == 60))
print(result)