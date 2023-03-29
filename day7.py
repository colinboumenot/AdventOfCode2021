text = [int(x) for x in open('InputTxt/day7input.txt', 'r').read().split(',')]

minimum = 0
for x in range(1,len(text)):
    minimum += abs(text[0] - text[x])

def sum_value(number):
    return_value = 0
    for x in text:
        return_value += abs(number - x)
    return return_value

for x in text:
    value = sum_value(x)
    minimum = min(value, minimum)
print(minimum)

def sum_everything(number):
    return number * (number + 1) // 2
results = []
for number in range(min(text), max(text) + 1):
    value = sum([sum_everything(abs(x-number)) for x in text])
    results.append(value)
print(min(results))
