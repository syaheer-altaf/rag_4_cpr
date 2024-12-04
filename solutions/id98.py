import math

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

def find_square_anagram_pairs(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)

    largest_square = 0
    for word_list in anagrams.values():
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                largest_square = max(largest_square, max_square_pair(word_list[i], word_list[j]))

    return largest_square

def max_square_pair(word1, word2):
    assignments = {}
    used_digits = [False] * 10
    return backtrack(word1, word2, 0, assignments, used_digits)

def backtrack(word1, word2, index, assignments, used_digits):
    if index == len(word1):
        if (word1[0] in assignments and assignments[word1[0]] == 0) or (word2[0] in assignments and assignments[word2[0]] == 0):
            return 0

        num1, num2 = 0, 0
        for c1, c2 in zip(word1, word2):
            num1 = num1 * 10 + assignments[c1]
            num2 = num2 * 10 + assignments[c2]

        if is_square(num1) and is_square(num2):
            return max(num1, num2)
        return 0

    if word1[index] in assignments:
        return backtrack(word1, word2, index + 1, assignments, used_digits)

    result = 0
    for i in range(10):
        if not used_digits[i]:
            used_digits[i] = True
            assignments[word1[index]] = i
            result = max(result, backtrack(word1, word2, index + 1, assignments, used_digits))
            del assignments[word1[index]]
            used_digits[i] = False

    return result

words = []
with open('words.txt', 'r') as file:
    content = file.read().strip()
    words = [word.strip('"') for word in content.split(",")]

largest_square = find_square_anagram_pairs(words)
print(largest_square)