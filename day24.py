text = open('InputTxt/day24input.txt')
data = [line.split('\n') for line in text.read().split('inp w\n')[1:]]
max = [0] * 14
min = [0] * 14
##print(data)
stack = []
for x, line in enumerate(data):
    if line[3] == 'div z 1':
        stack.append((x, int(line[14].split(' ')[-1])))
    elif line[3] == 'div z 26':
        y, z = stack.pop()
        difference = z + int(line[4].split(' ')[-1])
        if difference < 0:
            x, y, difference = y, x, -difference
        max[x] = 9
        max[y] = 9 - difference
        min[x] = 1 + difference
        min[y] = 1
print(''.join(map(str, max)))
print(''.join(map(str, min)))


