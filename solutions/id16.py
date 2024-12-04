def sum_of_digits_of_power(base, exponent):
    number = base ** exponent
    return sum(int(digit) for digit in str(number))

result = sum_of_digits_of_power(2, 1000)
print(result)