text = open('InputTxt/day1input.txt', 'r').read().splitlines()
s = set()
z = set()
total = 0
for x in range(1, len(text)):
    if int(text[x]) > int(text[x-1]):
        total += 1
print(total)

for x in range(len(text)):
    text[x] = int(text[x])

total = 0
for x in range(3, len(text)):
    if sum(text[x-2:x+1]) > sum(text[x-3:x]):
        total += 1
print(total)


