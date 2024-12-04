import random

board_size = 40
community_chest = [0, 10] + [None] * 14
chance = [0, 10, 11, 24, 39, 5, "next_r", "next_r", "next_u", -3] + [None] * 6
g2j = 30
railway = [5, 15, 25, 35]
utility = [12, 28]

def next_position(current, positions):
    for pos in positions:
        if pos > current:
            return pos
    return positions[0]

def simulate_game(turns, sides):
    position = 0
    frequencies = [0] * board_size
    doubles_count = 0
    random.shuffle(community_chest)
    random.shuffle(chance)
    cc_index, ch_index = 0, 0
    
    for _ in range(turns):
        die1, die2 = random.randint(1, sides), random.randint(1, sides)
        if die1 == die2:
            doubles_count += 1
        else:
            doubles_count = 0
        
        if doubles_count == 3:
            position = 10
            doubles_count = 0
        else:
            position = (position + die1 + die2) % board_size
        
        if position == g2j:
            position = 10
        elif position in [2, 17, 33]:
            if community_chest[cc_index] is not None:
                position = community_chest[cc_index]
            cc_index = (cc_index + 1) % len(community_chest)
        elif position in [7, 22, 36]:
            card = chance[ch_index]
            if card is not None:
                if card == "next_r":
                    position = next_position(position, railway)
                elif card == "next_u":
                    position = next_position(position, utility)
                elif card == -3:
                    position = (position - 3) % board_size
                else:
                    position = card
            ch_index = (ch_index + 1) % len(chance)
        
        frequencies[position] += 1
    
    return frequencies

turns = 10**6
sides = 4
frequencies = simulate_game(turns, sides)
top_squares = sorted(range(len(frequencies)), key=lambda x: -frequencies[x])[:3]
result = "".join(f"{square:02}" for square in top_squares)
print(result)