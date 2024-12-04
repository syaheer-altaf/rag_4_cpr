def last_ten_digits_of_series():
    total_sum = 0
    for i in range(1, 1001):
        total_sum += pow(i, i, 10**10)
        total_sum %= 10**10
    return total_sum

result = last_ten_digits_of_series()
print(result)