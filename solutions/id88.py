LIMIT = 12000
min_sum_product = [None] * (LIMIT + 1)

def factorize(n, remain, max_factor, sum_factors, num_terms):
    if remain == 1:
        if sum_factors > n:
            pass
        num_terms += n - sum_factors
        if num_terms <= LIMIT and (min_sum_product[num_terms] is None or n < min_sum_product[num_terms]):
            min_sum_product[num_terms] = n
    else:
        for i in range(2, max_factor + 1):
            if remain % i == 0:
                factor = i
                factorize(n, remain // factor, min(factor, max_factor), sum_factors + factor, num_terms + 1)

for i in range(2, LIMIT * 2 + 1):
    factorize(i, i, i, 0, 0)

result = sum(set(min_sum_product[2:]))
print(result)