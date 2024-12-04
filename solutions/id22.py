def name_value(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

def total_name_scores(filename):
    with open(filename, 'r') as f:
        names = f.read().replace('"', '').split(',')
    
    names.sort()
    
    total_score = 0
    for idx, name in enumerate(names, start=1):
        total_score += idx * name_value(name)
    
    return total_score

print(total_name_scores('names.txt'))