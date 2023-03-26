from collections import defaultdict
text = open('InputTxt/day5input.txt', 'r')

points = {}

for line in text:
    first, second = line.split('->')
    x1, x2 = min(int(first.strip().split(',')[0]), int(second.strip().split(',')[0])), max(int(first.strip().split(',')[0]), int(second.strip().split(',')[0]))
    y1, y2 = min(int(first.strip().split(',')[1]), int(second.strip().split(',')[1])), max(int(first.strip().split(',')[1]), int(second.strip().split(',')[1]))
    if x1 == x2 or y1 == y2:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x,y) not in points:
                    points[(x,y)] = 0
                points[(x,y)] += 1
answer = 0
for point in points:
    if points[point] > 1:
        answer += 1
print(answer)

text_two = open('InputTxt/day5input.txt', 'r')
points_two = defaultdict(int)

for line in text_two:
    first, second = line.split('->')
    x1, x2 = int(first.strip().split(',')[0]), int(second.strip().split(',')[0])
    y1, y2 = int(first.strip().split(',')[1]), int(second.strip().split(',')[1])
    dx = x2 - x1
    dy = y2 - y1

    for z in range(1 + max(abs(dx), abs(dy))):
        x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0)) * z
        y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0)) * z
        points_two[(x,y)] += 1

answer = 0
for point in points_two:
    if points_two[point] > 1:
        answer += 1
print(answer)