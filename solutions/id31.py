def count_ways_to_make_2():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    ways = [0] * (target + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]

result = count_ways_to_make_2()
print(result)