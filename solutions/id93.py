import itertools
import fractions

def longest_consecutive(abcd):
    a, b, c, d = abcd
    expressible = set()
    
    ops = [0, 0, 0, a, b, c, d]
    while True:
        
        for i in range(64):
            stack = []
            j = 0
            stackunderflow = False
            divbyzero = False
            
            for op in ops:
                if 1 <= op <= 9:
                    stack.append(fractions.Fraction(op))
                elif op == 0:
                    if len(stack) < 2:
                        stackunderflow = True
                        break
                    right = stack.pop()
                    left = stack.pop()
                    oper = (i >> (j * 2)) & 3
                    if oper == 0:
                        stack.append(left + right)
                    elif oper == 1:
                        stack.append(left - right)
                    elif oper == 2:
                        stack.append(left * right)
                    elif oper == 3:
                        if right.numerator == 0:
                            divbyzero = True
                            break
                        stack.append(left / right)
                    j += 1
                else:
                    pass

            if stackunderflow:
                break
            if divbyzero:
                continue
            if len(stack) != 1:
                pass

            result = stack.pop()
            if result.denominator == 1:
                expressible.add(result.numerator)
        
        if not next_permutation(ops):
            break
    
    return next(i for i in itertools.count(1) if i not in expressible) - 1

def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1:i - 1:-1]
    return True

max_consecutive = 0
best_abcd = None

for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                current_consecutive = longest_consecutive((a, b, c, d))
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
                    best_abcd = (a, b, c, d)

print("".join(str(x) for x in best_abcd))