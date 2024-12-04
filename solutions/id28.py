def sum_diagonals_in_spiral(size):
    total_sum = 1
    current_number = 1
    step = 2
    while step < size:
        for _ in range(4):
            current_number += step
            total_sum += current_number
        step += 2
    return total_sum

result = sum_diagonals_in_spiral(1001)
print(result)