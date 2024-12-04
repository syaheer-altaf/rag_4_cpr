count = 0
numerator, denominator = 3, 2

for _ in range(1000):
    if len(str(numerator)) > len(str(denominator)):
        count += 1
    numerator, denominator = numerator + 2 * denominator, numerator + denominator

print(count)