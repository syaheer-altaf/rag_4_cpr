def is_valid_arrangement(cube1, cube2):
    if (6 in cube1 or 9 in cube1):
        cube1.add(6)
        cube1.add(9)
    if (6 in cube2 or 9 in cube2):
        cube2.add(6)
        cube2.add(9)
    
    for a, b in SQUARES:
        if not ((a in cube1 and b in cube2) or (b in cube1 and a in cube2)):
            return False
    return True

def generate_square_pairs():
    return [(i**2 // 10, i**2 % 10) for i in range(1, 10)]

def count_valid_arrangements():
    valid_arrangements = 0
    for i in range(1 << 10):
        for j in range(i, 1 << 10):
            if bin(i).count('1') == 6 and bin(j).count('1') == 6:
                cube1 = {k for k in range(10) if (i & (1 << k)) != 0}
                cube2 = {k for k in range(10) if (j & (1 << k)) != 0}
                if is_valid_arrangement(cube1, cube2):
                    valid_arrangements += 1
    return valid_arrangements

SQUARES = generate_square_pairs()

result = count_valid_arrangements()
print(result)