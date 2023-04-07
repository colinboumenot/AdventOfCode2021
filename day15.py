import heapq
from collections import defaultdict
from math import inf as INFINITY
from itertools import filterfalse

text = open('InputTxt/day15input.txt')

grid = list(list(map(int, row)) for row in map(str.rstrip, text))

def adjacent(row, column, maxrow, maxcolumn):
    for x, y in ((1,0), (0,1), (-1,0), (0,-1)):
        newrow, newcolumn = (row + x, column + y)
        if 0 <= newrow < maxrow and 0 <= newcolumn < maxcolumn:
            yield newrow, newcolumn

def search(grid):
    x, y = len(grid), len(grid[0])
    start = (0,0)
    end = (x - 1, y - 1)
    queue = [(0, start)]
    visited = set()
    distance_dict = defaultdict(lambda : INFINITY, {start : 0})
    print(distance_dict)

    while queue:
        distance, location = heapq.heappop(queue)

        if location == end:
            return distance
        if location in visited:
            continue

        visited.add(location)
        row, column = location

        for adjacent_point in filterfalse(visited.__contains__, adjacent(row, column, x, y)):
            i, j = adjacent_point
            currentDistance = distance + grid[i][j]

            if currentDistance < distance_dict[adjacent_point]:
                distance_dict[adjacent_point] = currentDistance
                heapq.heappush(queue, (currentDistance, adjacent_point))
    return INFINITY
print(search(grid))

width = len(grid)
height = len(grid[0])

for _ in range(4):
    for row in grid:
        extension = row[-width:]
        row.extend((x + 1) if x < 9 else 1 for x in extension)
for _ in range(4):
    for row in grid[-height:]:
        row = [(x + 1) if x < 9 else 1 for x in row]
        grid.append(row)
print(search(grid))
