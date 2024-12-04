def e_continued_fraction_convergent(n):
    a = [2]
    for i in range(1, n):
        if i % 3 == 2:
            a.append(2 * (i // 3 + 1))
        else:
            a.append(1)

    h1, h2 = a[0], 1
    k1, k2 = 1, 0

    for i in range(1, n):
        h = a[i] * h1 + h2
        h2 = h1
        h1 = h
        k = a[i] * k1 + k2
        k2 = k1
        k1 = k

    return h1

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

convergent_numerator = e_continued_fraction_convergent(100)
digit_sum = sum_of_digits(convergent_numerator)
print(digit_sum)