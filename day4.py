text = [x for x in open('InputTxt/day4input.txt', 'r').read().splitlines()]
for x in range(1, len(text)):
    text[x] = text[x].strip().split()

bingo_moves = text[0].split(',')
boards = []

for f in range(2, len(text), 6):
    boards.append(text[f:f+5])

def move(number):
    for z in range(len(boards)):
        for x in range(len(boards[0][0])):
            for y in range(len(boards[0][0])):
                if int(boards[z][x][y]) == number:
                    boards[z][x][y] = -1
def is_winner():
    winner = -1
    for board in boards:
        for line in board:
            if len(set(line)) == 1:
                print('x')
                winner = board
                return winner
    for board in boards:
        for line in zip(*board):
            if len(line) > 1:
                if len(set(line)) == 1:
                    print('y')
                    winner = board
                    return winner
    return winner

index = -1
while is_winner() == -1:
    index += 1
    move(int(bingo_moves[index]))
winner_x = is_winner()
total = 0
last_played = int(bingo_moves[index])
for x in range(5):
    for y in range(5):
        if int(winner_x[x][y]) > 0:
            total += int(winner_x[x][y])
print(last_played)
print(total * last_played)

text = [x for x in open('InputTxt/day4input.txt', 'r').read().splitlines()]
for x in range(1, len(text)):
    text[x] = text[x].strip().split()

bingo_moves = text[0].split(',')
boards = []

for f in range(2, len(text), 6):
    boards.append(text[f:f+5])

def move(number):
    for z in range(len(boards)):
        for x in range(len(boards[0][0])):
            for y in range(len(boards[0][0])):
                if int(boards[z][x][y]) == number:
                    boards[z][x][y] = -1
def is_winner():
    for board in boards:
        for line in board:
            if len(set(line)) == 1:
                print('x')
                boards.remove(board)
    for board in boards:
        for line in zip(*board):
            if len(line) > 1:
                if len(set(line)) == 1:
                    boards.remove(board)

index = -1
while len(boards) != 1:
    index += 1
    is_winner()
    move(int(bingo_moves[index]))

winner_x = boards[0]
total = 0
last_played = int(bingo_moves[index])
for x in range(5):
    for y in range(5):
        if int(winner_x[x][y]) > 0:
            total += int(winner_x[x][y])
print(last_played)
print(total * last_played)


