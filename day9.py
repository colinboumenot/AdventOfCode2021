from math import prod
text = open('InputTxt/day9input.txt', 'r').read().strip().split('\n')
grid = [[int(x) for x in y] for y in text]


answer = 0
points = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if x > 0 and grid[x][y] >= grid[x-1][y]:
            continue
        if x < len(grid) - 1 and grid[x][y] >= grid[x+1][y]:
            continue
        if y > 0 and grid[x][y] >= grid[x][y-1]:
            continue
        if y < len(grid[0]) -1 and grid[x][y] >= grid[x][y+1]:
            continue
        answer += grid[x][y] + 1
        points.append((x,y))
print(answer)
print(points)

grid_two = {(x,y): int(z) for y,l in enumerate(open('InputTxt/day9input.txt'))
        for x,z in enumerate(l.strip())}

def adjacent(x,y):
    return filter(lambda n: n in grid_two,
    [(x,y-1), (x,y+1), (x-1,y), (x+1,y)])

def low_points(point):
    return all(grid_two[point] < grid_two[neighbor] for neighbor in adjacent(*point))

def basin_value(point):
    if grid_two[point] == 9: return 0
    del grid_two[point]
    return 1 + sum(map(basin_value, adjacent(*point)))

points = list(filter(low_points, grid_two))
basin = [basin_value(point) for point in points]
print(prod(sorted(basin)[-3:]))


