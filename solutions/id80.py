import math
from decimal import Decimal, getcontext

getcontext().prec = 110

def digital_sum_of_sqrt(n):
    sqrt_value = str(Decimal(n).sqrt()).replace('.', '')[:100]
    return sum(int(digit) for digit in sqrt_value)

total_sum = 0
for i in range(1, 101):
    if math.isqrt(i)**2 != i:
        total_sum += digital_sum_of_sqrt(i)

print(total_sum)