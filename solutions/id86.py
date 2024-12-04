import math
import itertools

def find_splits(a, b, c, limit, solutions):
    z = b
    for x in range(1, a):
        y = a - x
        if y < x:
            break
        if c * c == min(
                (x + y) * (x + y) + z * z,
                (y + z) * (y + z) + x * x,
                (z + x) * (z + x) + y * y):
            temp = max(x, y, z)
            if temp < limit:
                item = tuple(sorted((x, y, z)))
                solutions[temp].add(item)

def generate_solutions(limit, solutions):
    for s in itertools.count(3, 2):
        for t in range(s - 2, 0, -2):
            if s * s // 2 >= limit * 3:
                return
            if math.gcd(s, t) == 1:
                for k in itertools.count(1):
                    a = s * t * k
                    b = (s * s - t * t) // 2 * k
                    c = (s * s + t * t) // 2 * k
                    if a >= limit and b >= limit:
                        break
                    find_splits(a, b, c, limit, solutions)
                    find_splits(b, a, c, limit, solutions)

def find_cumulative_solutions(limit):
    solutions = []
    cumulativesolutions = [0]
    
    while True:
        while len(solutions) < limit:
            solutions.append(set())
        
        generate_solutions(limit, solutions)
        
        for i in range(len(cumulativesolutions), limit):
            cumulative_sum = cumulativesolutions[i - 1] + len(solutions[i])
            cumulativesolutions.append(cumulative_sum)
            if cumulative_sum > 1000000:
                return i
        
        limit *= 2

limit = 1
result = find_cumulative_solutions(limit)
print(result)