def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def find_pair():
    pentagonals = set()
    min_d = float('inf')
    j = 1
    while True:
        pj = pentagonal(j)
        for k in range(j-1, 0, -1):
            pk = pentagonal(k)
            if is_pentagonal(pj + pk) and is_pentagonal(abs(pj - pk)):
                d = abs(pj - pk)
                if d < min_d:
                    min_d = d
        pentagonals.add(pj)
        j += 1
        if min_d != float('inf'):
            return min_d

result = find_pair()
print(result)