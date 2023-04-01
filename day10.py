text =[x for x in open('InputTxt/day10input.txt', 'r').read().strip().split('\n')]

characters = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
begin = list(characters.keys())

for (key, value) in list(characters.items()):
    characters[value] = key

answer = 0
for line in text:
    stack = []
    for character in line:
        if character in begin:
            stack = [character] + stack
        else:
            if not stack:
                break
            correct = characters[stack[0]]
            stack = stack[1:]
            if correct == character:
                continue
            answer += points[character]
            break
print(answer)

text_two =[x for x in open('InputTxt/day10input.txt', 'r').read().strip().split('\n')]

characters_two = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
points_two = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
begin_two = list(characters.keys())
for (key, value) in list(characters_two.items()):
    characters_two[value] = key

costs = []

for line in text_two:
    stack = []
    done = False
    for character in line:
        if character in begin:
            stack = [character] + stack
        else:
            if not stack:
                break
            correct = characters_two[stack[0]]
            stack = stack[1:]
            if correct == character:
                continue
            done = True
            break
    if not done:
        x = 0
        for character in stack:
            x = x * 5 + points_two[characters_two[character]]
        costs += [x]

costs = sorted(costs)
print(costs[len(costs)//2])