import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture_check(n):
    for i in range(1, int(math.sqrt(n // 2)) + 1):
        if is_prime(n - 2 * i * i):
            return True
    return False

def find_counterexample():
    n = 9
    while True:
        if n % 2 == 1 and not is_prime(n):
            if not goldbach_conjecture_check(n):
                return n
        n += 2

result = find_counterexample()
print(result)