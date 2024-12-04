def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
    return max_palindrome

result = largest_palindrome_product()
print(result)