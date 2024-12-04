def rank_value(card):
    ranks = '23456789TJQKA'
    return ranks.index(card[0])

def evaluate_hand(hand):
    ranks = sorted([rank_value(card) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    rank_counts = {r: ranks.count(r) for r in ranks}
    sorted_counts = sorted(rank_counts.items(), key=lambda x: (-x[1], -x[0]))
    counts = [x[1] for x in sorted_counts]
    sorted_ranks = [x[0] for x in sorted_counts]
    is_flush = len(set(suits)) == 1
    is_straight = len(counts) == 5 and ranks[0] - ranks[-1] == 4
    if is_straight and is_flush:
        return (8, ranks)
    if counts == [4, 1]:
        return (7, sorted_ranks)
    if counts == [3, 2]:
        return (6, sorted_ranks)
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, ranks)
    if counts == [3, 1, 1]:
        return (3, sorted_ranks)
    if counts == [2, 2, 1]:
        return (2, sorted_ranks)
    if counts == [2, 1, 1, 1]:
        return (1, sorted_ranks)
    return (0, ranks)

def determine_winner(player1, player2):
    rank1, values1 = evaluate_hand(player1)
    rank2, values2 = evaluate_hand(player2)
    if rank1 > rank2:
        return 1
    if rank1 < rank2:
        return 2
    return 1 if values1 > values2 else 2

with open("poker.txt") as f:
    hands = f.read().strip().split("\n")

player1_wins = 0
for line in hands:
    cards = line.split()
    player1 = cards[:5]
    player2 = cards[5:]
    if determine_winner(player1, player2) == 1:
        player1_wins += 1

print(player1_wins)