def get_terminal(n, terminal_cache):
    while n not in terminal_cache:
        n = square_digit_sum(n)
    return n

def square_digit_sum(n):
    result = 0
    while n > 0:
        digit = n % 10
        result += digit * digit
        n //= 10
    return result

terminal_cache = {1, 89}
starting_numbers_count = 0

for i in range(1, 10000000):
    if get_terminal(i, terminal_cache) == 89:
        starting_numbers_count += 1

print(starting_numbers_count)