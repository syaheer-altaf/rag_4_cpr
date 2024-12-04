def collatz_chain_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    memo[n] = 1 + collatz_chain_length(next_n, memo)
    return memo[n]

def longest_collatz_sequence(limit):
    memo = {}
    max_length = 0
    starting_number = 0
    for i in range(1, limit):
        length = collatz_chain_length(i, memo)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number

result = longest_collatz_sequence(1000000)
print(result)