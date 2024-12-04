import math

def continued_fraction_period(N):
    m = 0
    d = 1
    a0 = int(math.sqrt(N))
    if a0 * a0 == N:
        return 0
    a = a0
    period = 0
    while a != 2 * a0:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        period += 1
    return period

def count_odd_periods(limit):
    count = 0
    for N in range(2, limit + 1):
        if int(math.sqrt(N)) ** 2 != N:
            period = continued_fraction_period(N)
            if period % 2 == 1:
                count += 1
    return count

print(count_odd_periods(10000))