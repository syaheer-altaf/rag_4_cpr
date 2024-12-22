import itertools

def read_sets(file_path):
    with open(file_path, 'r') as file:
        sets = [list(map(int, line.strip().split(','))) for line in file]
    return sets

def is_special_sum_set(s):
    sums_seen = set()
    min_sum = [None] * (len(s) + 1)
    max_sum = [None] * (len(s) + 1)

    def explore_subsets(i, count, total):
        if i == len(s):
            sums_seen.add(total)
            if min_sum[count] is None or total < min_sum[count]:
                min_sum[count] = total
            if max_sum[count] is None or total > max_sum[count]:
                max_sum[count] = total
        else:
            explore_subsets(i + 1, count, total)
            explore_subsets(i + 1, count + 1, total + s[i])

    explore_subsets(0, 0, 0)
    return len(sums_seen) == 2 ** len(s) and all(max_sum[i] < min_sum[i + 1] for i in range(len(s)))

def get_special_sum_sets(sets):
    return [s for s in sets if is_special_sum_set(s)]

def sum_of_special_sum_sets(sets):
    return sum(sum(s) for s in get_special_sum_sets(sets))

SETS = read_sets('sets.txt')
result = sum_of_special_sum_sets(SETS)
print(result)