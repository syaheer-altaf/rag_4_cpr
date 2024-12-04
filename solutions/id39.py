def pythagorean_triplets(limit):
    solutions = [0] * (limit + 1)
    
    for a in range(1, limit // 2):
        for b in range(a, (limit - a) // 2):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and a + b + int(c) <= limit:
                solutions[a + b + int(c)] += 1
                
    return solutions

def max_solutions(limit):
    solutions = pythagorean_triplets(limit)
    return solutions.index(max(solutions))

print(max_solutions(1000))