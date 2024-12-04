def digit_sum(n):
    return sum(int(d) for d in str(n))

max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        max_sum = max(max_sum, digit_sum(a ** b))

print(max_sum)