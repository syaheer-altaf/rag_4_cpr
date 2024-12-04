def count_combinations(limit, max_n):
    count = 0
    for n in range(1, max_n + 1):
        c = 1
        for r in range(0, n // 2 + 1):
            if c > limit:
                count += (n - 2 * r + 1)  # Account for symmetry
                break
            c = c * (n - r) // (r + 1)
    return count

print(count_combinations(10**6, 100))