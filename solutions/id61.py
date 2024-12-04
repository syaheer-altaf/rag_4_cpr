import itertools

def figurate_number(sides, n):
    return n * ((sides - 2) * n - (sides - 4)) // 2

def find_cyclic_figurate_sum():
    numbers_by_prefix = [[set() for _ in range(100)] for _ in range(9)]
    
    for sides in range(3, 9):
        for n in itertools.count(1):
            num = figurate_number(sides, n)
            if num >= 10000:
                break
            if num >= 1000:
                numbers_by_prefix[sides][num // 100].add(num)
    
    def find_cyclic_sum(start, current, sides_used, total_sum):
        if sides_used == 0b111111000:
            if current % 100 == start // 100:
                return total_sum
        else:
            for sides in range(4, 9):
                if (sides_used >> sides) & 1 != 0:
                    continue
                for num in numbers_by_prefix[sides][current % 100]:
                    result = find_cyclic_sum(start, num, sides_used | (1 << sides), total_sum + num)
                    if result is not None:
                        return result
            return None
    
    for prefix in range(10, 100):
        for num in numbers_by_prefix[3][prefix]:
            result = find_cyclic_sum(num, num, 1 << 3, num)
            if result is not None:
                return str(result)
    
    raise AssertionError("No solution")

print(find_cyclic_figurate_sum())