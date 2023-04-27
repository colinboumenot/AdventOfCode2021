text = open('InputTxt/day25input.txt').read()
grid = [list(line) for line in text.splitlines()]
final = 0
while True:
    final += 1
    count = 0
    moves = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '>' and grid[x][(y+1) % len(grid[0])] == '.':
                moves.append((x, y))
    for x, y in moves:
        grid[x][y] = '.'
        grid[x][(y+1) % len(grid[0])] = '>'
    count += len(moves)
    moves.clear()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'v' and grid[(x + 1) % len(grid)][y] == '.':
                moves.append((x,y))
    for x, y in moves:
        grid[x][y] = '.'
        grid[(x + 1) % len(grid)][y] = 'v'
    count += len(moves)
    if count == 0:
        print(final)
        break


