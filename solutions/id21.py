def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def amicable_numbers(limit):
    amicable_sum = 0
    visited = set()
    
    for a in range(2, limit):
        if a not in visited:
            b = sum_of_divisors(a)
            if b != a and sum_of_divisors(b) == a:
                amicable_sum += a + b
                visited.add(a)
                visited.add(b)
                
    return amicable_sum

result = amicable_numbers(10000)
print(result)