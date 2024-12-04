def has_same_digits(x):
    digits = sorted(str(x))
    for multiplier in range(2, 7):
        if sorted(str(x * multiplier)) != digits:
            return False
    return True

x = 1
while True:
    if has_same_digits(x):
        print(x)
        break
    x += 1