text = open('InputTxt/day2input.txt', 'r').read().splitlines()

depth = 0
horizontal = 0

for line in text:
    cmd, value = line.split()
    if cmd == 'forward':
        horizontal += int(value)
    elif cmd == 'up':
        depth -= int(value)
    else:
        depth += int(value)
print(horizontal * depth)

depth = 0
horizontal = 0
aim = 0

for line in text:
    cmd, value = line.split()
    if cmd == 'forward':
        horizontal += int(value)
        depth += aim * int(value)
    elif cmd == 'up':
        aim -= int(value)
    else:
        aim += int(value)
print(horizontal * depth)