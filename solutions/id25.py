def fibonacci_index_with_digits(digits):
    a, b = 1, 1
    index = 2
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= digits:
            return index

result = fibonacci_index_with_digits(1000)
print(result)