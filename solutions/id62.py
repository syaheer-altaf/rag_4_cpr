def find_smallest_cube_with_permutations(n_permutations):
    cubes = {}
    num = 1
    while True:
        cube = num ** 3
        sorted_digits = ''.join(sorted(str(cube)))
        if sorted_digits not in cubes:
            cubes[sorted_digits] = []
        cubes[sorted_digits].append(cube)
        
        if len(cubes[sorted_digits]) == n_permutations:
            return min(cubes[sorted_digits])
        
        num += 1

result = find_smallest_cube_with_permutations(5)
print(result)