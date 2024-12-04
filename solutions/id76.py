def count_partitions(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

result = count_partitions(100)
print(result)