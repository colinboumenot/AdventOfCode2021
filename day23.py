
rooms = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

positions = set(rooms.values())

costs = {
    'A' : 1,
    'B' : 10,
    'C' : 100,
    'D' : 1000,
}

def legal(board, x1, x2):
    a = min(x1, x2)
    b = max(x1, x2)
    for x in range(a, b + 1):
        if x == x1 or x in positions:
            continue
        if board[x] != '.':
            return False
    return True

def finished(board, piece, x):
    return len(board[x]) == board[x].count('.') + board[x].count(piece)

def get_piece(room):
    for x in room:
        if x != '.':
            return x

def possibilities(board, x):
    piece = board[x]
    if x not in positions:
        if legal(board, x, rooms[piece]) and finished(board, piece, rooms[piece]):
            return [rooms[piece]]
        return []

    move = get_piece(piece)
    if x == rooms[move] and finished(board, move, x):
        return []

    possible = []
    for y in range(len(board)):
        if y == x or (y in positions and rooms[move] != y):
            continue
        if rooms[move] == y:
            if not finished(board, move, y):
                continue
        if legal(board, x, y):
            possible.append(y)
    return possible

def relocate(x, room):
    room = list(room)
    distance = room.count('.')
    room[distance - 1] = x
    return ''.join(room), distance

def move(board, x, y):
    board_x = board[:]
    distance = 0
    move = get_piece(board[x])
    if len(board[x]) == 1:
        board_x[x] = '.'
    else:
        room = ''
        found = False
        for space in board[x]:
            if space == '.':
                distance += 1
                room += space
            elif not found:
                room += '.'
                distance += 1
                found = True
            else:
                room += space
        board_x[x] = room
    distance += abs(x - y)
    if len(board[y]) == 1:
        board_x[y] = move
        return board_x, distance * costs[move]
    else:
        board_x[y], distance_x = relocate(move, board[y])
        distance += distance_x
        return board_x, distance * costs[move]

def stuff(board):
    locations = {tuple(board) : 0}
    queue = [board]
    while queue:
        board = queue.pop()
        for x, y in enumerate(board):
            if get_piece(y) is None:
                continue
            possible = possibilities(board, x)
            for possibility in possible:
                board_x, cost = move(board, x, possibility)
                newcost = locations[tuple(board)] + cost
                board_y = tuple(board_x)
                total_cost = locations.get(board_y, 9999999)
                if newcost < total_cost:
                    locations[board_y] = newcost
                    queue.append(board_x)
    return locations

board = ['.', '.', 'DD', '.', 'CC', '.', 'AB', '.', 'BA', '.', '.']
answer = stuff(board)
print(answer[('.', '.', 'AA', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.')])
board_two = ['.', '.', 'DDDD', '.', 'CCBC', '.', 'ABAB', '.', 'BACA', '.', '.']
answer_two = stuff(board_two)
print(answer_two[('.', '.', 'AAAA', '.', 'BBBB', '.', 'CCCC', '.', 'DDDD', '.', '.')])