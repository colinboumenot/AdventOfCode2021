from collections import Counter
from collections import defaultdict
text = open('InputTxt/day21input.txt').read().splitlines()

player_one_position = int(text[0].split(': ')[1])
player_two_position = int(text[1].split(': ')[1])
player_one = 0
player_two = 0

rolls = 0
roll = 1

while player_one < 1000 and player_two < 1000:
    for _ in range(3):
        if roll % 100 == 0:
            player_one_position += 100
        else:
            player_one_position += roll % 100
        roll += 1
    rolls += 3
    if player_one_position % 10 == 0:
        player_one += 10
        if player_one >= 1000:
            break
    else:
        player_one += player_one_position % 10
        if player_one >= 1000:
            break
    for _ in range(3):
        if roll % 100 == 0:
            player_two_position += 100
        else:
            player_two_position += roll % 100
        roll += 1
    rolls += 3
    if player_two_position % 10 == 0:
        player_two += 10
    else:
        player_two += player_two_position % 10

player_one_universe = 10
player_two_universe = 6
dice = list(Counter(x + y + z for x in range(1,4) for y in range(1,4) for z in range(1,4)).items())
universes = {(0, player_one_universe, 0, player_two_universe): 1}
player_one_wins = 0
player_two_wins = 0
while universes:
    universe = defaultdict(int)
    for item, count in list(universes.items()):
        score_one, position_one, score_two, position_two = item
        for index, dice_count in dice:
            player_1 = (position_one + index - 1) % 10 + 1
            score_1 = score_one + player_1
            if score_1 >= 21:
                player_one_wins += dice_count * count
                continue
            for index_two, dice_count_two in dice:
                player_2 = (position_two + index_two - 1) % 10 + 1
                score_2 = score_two + player_2
                if score_2 >= 21:
                    player_two_wins += count * dice_count * dice_count_two
                    continue
                universe[(score_1, player_1, score_2, player_2)] += count * dice_count * dice_count_two
    universes = universe
print(player_one_wins)
print(player_two_wins)




