text = open('InputTxt/day13input.txt', 'r')

lines = [line.strip() for line in text]
partition = lines.index("")
grid = set(tuple(map(int, line.split(","))) for line in lines[:partition])

for command in lines[partition + 1:]:
    axis, position = command.split()[2].split('=')
    position = int(position)
    update = set()
    for x, y in grid:
        if axis == 'x' and x > position:
            update.add((2 * position - x, y))
        elif axis == 'y' and y > position:
            update.add((x, 2 * position - y))
        else:
            update.add((x,y))
    grid = update
    print(len(grid))
minX = min(x for x,y in grid)
minY = min(y for x,y in grid)
maxX = max(x for x,y in grid)
maxY = max(y for x,y in grid)
for y in range(minY, maxY + 1):
    print(''.join('#' if (x,y) in grid else '.' for x in range(minX, maxX +1)))


