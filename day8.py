from collections import Counter
text = open('InputTxt/day8input.txt', 'r').read().strip().split('\n')

answer = 0
for line in text:
    x,y = line.split('|')
    data = y.split(' ')
    for i in data:
        if len(i) in (2,3,4,7):
            answer += 1
print(answer)

def translate(x):
    return Counter(list(x.replace(' ', '')))

def pattern(x, y):
    return tuple(sorted([y[z] for z in x]))

strings = 'abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg'
string_dict = translate(strings)
translator = {}
for index, x in enumerate(strings.split(' ')):
    translator[pattern(x, string_dict)] = index

answer = 0
for line in text:
    x = line.split(' | ')[1].strip()
    y = translate(line.split(' | ')[0])
    data = [translator[pattern(z, y)] for z in x.split(' ')]
    answer += int(''.join([str(w) for w in data]))
print(answer)



