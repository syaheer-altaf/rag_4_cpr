from itertools import permutations

def check_property(pandigital):
    return (
        int(pandigital[1:4]) % 2 == 0 and
        int(pandigital[2:5]) % 3 == 0 and
        int(pandigital[3:6]) % 5 == 0 and
        int(pandigital[4:7]) % 7 == 0 and
        int(pandigital[5:8]) % 11 == 0 and
        int(pandigital[6:9]) % 13 == 0 and
        int(pandigital[7:10]) % 17 == 0
    )

pandigital_numbers = [''.join(map(str, p)) for p in permutations(range(10))]
valid_numbers = [int(num) for num in pandigital_numbers if check_property(num)]
result = sum(valid_numbers)
print(result)