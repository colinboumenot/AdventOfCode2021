text = open('InputTxt/day6input.txt', 'r').readlines()
text = list(map(int, text[0].strip().split(',')))

fishes = [text.count(x) for x in range(9)]

for x in range(80):
    value = fishes.pop(0)
    fishes[6] += value
    fishes.append(value)
print(sum(fishes))

text = open('InputTxt/day6input.txt', 'r').readlines()
text = list(map(int, text[0].strip().split(',')))

fishes = [text.count(x) for x in range(9)]

for x in range(256):
    value = fishes.pop(0)
    fishes[6] += value
    fishes.append(value)
print(sum(fishes))