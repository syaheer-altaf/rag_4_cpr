def recurring_cycle_length(d):
    remainders = {}
    numerator = 1
    position = 0
    while numerator != 0:
        if numerator in remainders:
            return position - remainders[numerator]
        remainders[numerator] = position
        numerator = (numerator % d) * 10
        position += 1
    return 0

def find_longest_recurring_cycle(limit):
    max_cycle_length = 0
    result = 0
    for d in range(2, limit):
        cycle_length = recurring_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = d
    return result

result = find_longest_recurring_cycle(1000)
print(result)