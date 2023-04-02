from collections import defaultdict
text = open('InputTxt/day12input.txt', 'r').read().splitlines()

adjacent = defaultdict(list)

for line in text:
    left, right = line.split('-')
    adjacent[left].append(right)
    adjacent[right].append(left)

def dfs(current, end, big = False, used = frozenset()):
    answer = 0
    for adjacent_point in adjacent[current]:
        if adjacent_point == 'start':
            continue
        if current.islower():
            used = used.union([current])
        if adjacent_point == end:
            answer += 1
        elif adjacent_point in used:
            if big:
                answer += dfs(adjacent_point, end, False, used)
        else:
            answer += dfs(adjacent_point, end, big, used)
    return answer


print(dfs('start', 'end'))
print(dfs('start', 'end', True))


