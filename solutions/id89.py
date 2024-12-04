def roman_to_int(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def int_to_roman(num):
    roman_dict = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ""
    for value, symbol in roman_dict:
        while num >= value:
            roman += symbol
            num -= value
    return roman

def count_characters_saved(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    saved_characters = 0
    for line in lines:
        line = line.strip()
        roman_len = len(line)
        minimal_roman = int_to_roman(roman_to_int(line))
        minimal_len = len(minimal_roman)
        saved_characters += roman_len - minimal_len

    return saved_characters

print(count_characters_saved("roman.txt"))