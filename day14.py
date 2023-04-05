from collections import Counter
from collections import defaultdict
text = open('InputTxt/day14input.txt', 'r')
lines = [line.strip() for line in text.readlines()]
start = lines[0]
rules = [rule.split(' ') for rule in lines[2:]]
rules = {a: (a[0] + c, c + a[1]) for a,b,c in rules}
polymer = [''.join(chain) for chain in zip(start, start[1:])]
STEPS = 40

counter = Counter(polymer)
for x in range(STEPS):
    new_counter = {key : 0 for key in rules.keys()}
    for key, value in counter.items():
        new_counter[rules[key][0]] += value
        new_counter[rules[key][1]] += value
    counter = new_counter

letters_two = defaultdict(int)
for key, value in counter.items():
    letters_two[key[0]] += value

letters_two[start[-1]] += 1
maxLetter = max(letters_two.values())
minLetter = min(letters_two.values())
print(maxLetter - minLetter)
