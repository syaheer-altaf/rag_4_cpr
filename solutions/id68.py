import itertools

def is_valid_ring(ring):
    return (
        ring[0] + ring[5] + ring[6] == 
        ring[1] + ring[6] + ring[7] == 
        ring[2] + ring[7] + ring[8] == 
        ring[3] + ring[8] + ring[9] == 
        ring[4] + ring[9] + ring[5]
    )

def generate_maximum_ring():
    best_ring = None
    numbers = list(range(1, 11))
    
    for perm in itertools.permutations(numbers):
        if is_valid_ring(perm):
            min_outer_index = min(range(5), key=lambda i: perm[i])
            
            current_ring = ""
            for i in range(5):
                current_ring += str(perm[(min_outer_index + i) % 5])
                current_ring += str(perm[(min_outer_index + i) % 5 + 5])
                current_ring += str(perm[(min_outer_index + i + 1) % 5 + 5])

            if len(current_ring) == 16 and (best_ring is None or current_ring > best_ring):
                best_ring = current_ring

    return best_ring

result = generate_maximum_ring()
print(result)