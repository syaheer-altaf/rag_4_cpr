count = 0
for n in range(1, 100):
    base = 1
    while True:
        power = base ** n
        if len(str(power)) > n:
            break
        if len(str(power)) == n:
            count += 1
        base += 1
print(count)