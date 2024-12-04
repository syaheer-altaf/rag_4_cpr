def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1

print(count)