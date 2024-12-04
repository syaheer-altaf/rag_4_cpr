import itertools

def read_ciphertext(file_path):
    with open(file_path, 'r') as file:
        cipher_data = file.read().strip()
    return list(map(int, cipher_data.split(',')))

def calculate_score(plaintext):
    score = 0
    for char in plaintext:
        if 65 <= char <= 90:
            score += 1
        elif 97 <= char <= 122:
            score += 2
        elif char < 0x20 or char == 0x7F:
            score -= 10
    return score

def decrypt_message(ciphertext, key):
    return [(char ^ key[i % len(key)]) for i, char in enumerate(ciphertext)]

def find_best_key(file_path):
    ciphertext = read_ciphertext(file_path)
    
    best_key = max(
        ((x, y, z) for x in range(97, 123) for y in range(97, 123) for z in range(97, 123)),
        key=lambda key: calculate_score(decrypt_message(ciphertext, key))
    )
    
    decrypted_text = decrypt_message(ciphertext, best_key)
    
    ascii_sum = sum(decrypted_text)
    
    decrypted_message = ''.join(chr(char) for char in decrypted_text)
    
    print(f"Decrypted message: {decrypted_message}")
    
    return str(ascii_sum)

file_path = '0059_cipher.txt'
result = find_best_key(file_path)
print(f"Sum of ASCII values in the decrypted message: {result}")