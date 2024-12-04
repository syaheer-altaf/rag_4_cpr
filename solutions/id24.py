def find_lexicographic_permutation(n):
    digits = list(range(10))
    permutation = []
    n -= 1
    factorial = 1
    for i in range(1, len(digits)):
        factorial *= i

    while digits:
        index = n // factorial
        permutation.append(digits.pop(index))
        n %= factorial
        if digits:
            factorial //= len(digits)

    return ''.join(map(str, permutation))

result = find_lexicographic_permutation(1000000)
print(result)