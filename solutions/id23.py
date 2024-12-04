def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def find_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(12, limit):
        if sum_of_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def cannot_be_written_as_sum_of_abundant_numbers(limit):
    abundant_numbers = find_abundant_numbers(limit)
    can_be_written = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundant <= limit:
                can_be_written[sum_abundant] = True

    total_sum = sum(i for i in range(1, limit + 1) if not can_be_written[i])
    return total_sum

result = cannot_be_written_as_sum_of_abundant_numbers(28123)
print(result)