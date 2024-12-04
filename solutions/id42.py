def is_triangle_number(n):
    x = (8 * n + 1) ** 0.5
    return x == int(x)

def word_value(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

def count_triangle_words(filename):
    with open(filename, 'r') as f:
        words = f.read().replace('"', '').split(',')
    
    count = 0
    for word in words:
        if is_triangle_number(word_value(word)):
            count += 1
    
    return count

print(count_triangle_words('words.txt'))