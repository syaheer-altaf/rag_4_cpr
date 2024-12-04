import math

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return lines

def compare_base_exp(base_exp):
    base, exp = map(int, base_exp.split(','))
    return exp * math.log(base)

def find_greatest_value(filename):
    lines = read_file(filename)
    max_value = float('-inf')
    line_number = -1

    for i, line in enumerate(lines):
        value = compare_base_exp(line)
        if value > max_value:
            max_value = value
            line_number = i + 1

    return line_number

result = find_greatest_value('base_exp.txt')
print(result)