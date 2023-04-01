text = open('InputTxt/day11input.txt', 'r')

grid = {(x,y): int(point) for x, line in enumerate(text) for y, point in enumerate(line.strip())}

def adjacent(point):
    x = point[0]
    y = point[1]
    return filter(grid.get, [(x-1,y), (x+1,y), (x,y-1), (x,y+1),
                             (x-1,y-1), (x+1,y+1), (x+1, y-1), (x-1,y+1)])

answer = 0
for x in range(0,1000000000000000000000):
    for point in grid:
        grid[point] += 1
    flashes = {point for point in grid if grid[point] > 9}

    while flashes:
        point = flashes.pop()
        grid[point] = 0
        answer += 1
        for p in adjacent(point):
            grid[p] += 1
            if grid[p] > 9:
                flashes.add(p)
    if x == 99:
        print(answer)
    if sum(grid.values()) == 0:
        print(x+1)
        break


