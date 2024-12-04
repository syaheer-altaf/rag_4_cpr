def is_pandigital(num_str):
    return len(num_str) == 9 and set(num_str) == set("123456789")

def concatenated_product(n, m):
    return "".join(str(n * i) for i in range(1, m+1))

def largest_pandigital_concatenated_product():
    largest = 0
    for n in range(1, 10000):
        for m in range(2, 10):
            product = concatenated_product(n, m)
            if len(product) == 9 and is_pandigital(product):
                largest = max(largest, int(product))
    return largest

print(largest_pandigital_concatenated_product())
