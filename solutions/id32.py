def is_pandigital(a, b, product):
    digits = str(a) + str(b) + str(product)
    return ''.join(sorted(digits)) == '123456789'

def find_pandigital_products():
    products = set()
    for a in range(1, 100):
        for b in range(a, 10000 // a):
            product = a * b
            if is_pandigital(a, b, product):
                products.add(product)
    return sum(products)

result = find_pandigital_products()
print(result)