def pentagonal_number(k):
    return k * (3 * k - 1) // 2

def partition_function(limit, modulus):
    partitions = [1]
    n = 1
    while True:
        partitions.append(0)
        k = 1
        while True:
            pentagonal = pentagonal_number(k)
            if pentagonal > n:
                break
            sign = -1 if (k % 2 == 0) else 1
            partitions[n] += sign * partitions[n - pentagonal]
            partitions[n] %= modulus
            k += 1
        k = -1
        while True:
            pentagonal = pentagonal_number(k)
            if pentagonal > n:
                break
            sign = -1 if (k % 2 == 0) else 1
            partitions[n] += sign * partitions[n - pentagonal]
            partitions[n] %= modulus
            k -= 1
        if partitions[n] == 0:
            return n
        n += 1

print(partition_function(1000000, 1000000))