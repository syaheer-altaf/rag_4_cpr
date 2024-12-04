def distinct_powers(limit):
    terms = set()
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            terms.add(a ** b)
    return len(terms)

result = distinct_powers(100)
print(result)