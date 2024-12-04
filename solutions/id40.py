def find_digit(n):
    length = 1
    count = 9
    start = 1
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    
    num = start + (n - 1) // length
    digit = str(num)[(n - 1) % length]
    return int(digit)

digits = [find_digit(10**i) for i in range(7)]
result = 1
for digit in digits:
    result *= digit

print(result)