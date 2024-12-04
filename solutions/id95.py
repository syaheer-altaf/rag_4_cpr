import itertools

LIMIT = 10**6

divisor_sum = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
    for j in range(i * 2, LIMIT + 1, i):
        divisor_sum[j] += i

max_chain_length = 0
smallest_member = -1

for start in range(LIMIT + 1):
    visited = set()
    current = start
    for count in itertools.count(1):
        visited.add(current)
        next_number = divisor_sum[current]
        if next_number == start:
            if count > max_chain_length:
                smallest_member = start
                max_chain_length = count
            break
        elif next_number > LIMIT or next_number in visited:
            break
        else:
            current = next_number

print(smallest_member)