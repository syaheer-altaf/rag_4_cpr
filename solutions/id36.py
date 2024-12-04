def is_palindromic(n):
    return str(n) == str(n)[::-1]

def sum_palindromic_numbers(limit):
    total_sum = 0
    for i in range(1, limit):
        if is_palindromic(i) and is_palindromic(bin(i)[2:]):
            total_sum += i
    return total_sum

result = sum_palindromic_numbers(1000000)
print(result)