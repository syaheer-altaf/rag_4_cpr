import itertools

def is_subsequence(short_str, long_str):
    i = 0
    for char in long_str:
        if char == short_str[i]:
            i += 1
            if i == len(short_str):
                return True
    return False

def is_consistent(guess):
    return all(is_subsequence(seq, guess) for seq in subsequences)

def find_passcode():
    chars_used = sorted(set().union(*subsequences))
    base = len(chars_used)
    
    for length in itertools.count(base):
        indices = [0] * length
        while True:
            guess = "".join(chars_used[d] for d in indices)
            if is_consistent(guess):
                return guess
            
            i = 0
            while i < length and indices[i] == base - 1:
                indices[i] = 0
                i += 1
            if i == length:
                break
            indices[i] += 1

with open("keylog.txt") as file:
    subsequences = [line.strip() for line in file]

result = find_passcode()
print(result)