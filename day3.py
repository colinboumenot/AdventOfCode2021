from collections import Counter
text = open('InputTxt/day3input.txt', 'r')

result = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ]

for line in text.read().splitlines():
    for x in range(len(line)):
        if int(line[x]) == 0:
            result[x][0] += 1
        else:
            result[x][1] += 1

gamma_rate = '000000000000'
epsilon_rate = '000000000000'

for x in range(len(result)):
    if result[x][1] > result[x][0]:
        gamma_rate = gamma_rate[:x] + '1' + gamma_rate[x+1:]
    else:
        epsilon_rate = epsilon_rate[:x] + '1' + epsilon_rate[x + 1:]
print(int(gamma_rate, 2) * int(epsilon_rate, 2))

oxygen_rate = ''
scrubber_rate = ''
text_copy = [x for x in open('InputTxt/day3input.txt', 'r').read().splitlines()]
for x in range(len(text_copy[0])):
    count = Counter(y[x] for y in text_copy)
    if count['0'] > count['1']:
        text_copy = [y for y in text_copy if y[x] == '1']
    else:
        text_copy = [y for y in text_copy if y[x] == '0']
    if text_copy:
        scrubber_rate = text_copy[0]

text_copy = [x for x in open('InputTxt/day3input.txt', 'r').read().splitlines()]
for x in range(len(text_copy[0])):
    count = Counter(y[x] for y in text_copy)
    if count['0'] > count['1']:
        text_copy = [y for y in text_copy if y[x] == '0']
    else:
        text_copy = [y for y in text_copy if y[x] == '1']
    if text_copy:
        oxygen_rate = text_copy[0]
print(int(oxygen_rate,2) * int(scrubber_rate,2))


