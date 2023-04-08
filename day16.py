text = open('InputTxt/day16input.txt', 'r')
data = [x for x in text.read().strip().split('\n')]

translate = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

data = ''.join([translate[x] for x in data[0]])
summation = 0
def process(packet):
    global summation
    version = packet[0:3]
    idtype = packet[3:6]
    summation += (int(version, 2))
    print(summation)

    if idtype == '100':
        index = 6
        num = ''
        while True:
            num += packet[index+1:index+5]
            if packet[index] == '0':
                break
            index += 5
        return index + 5, int(num, 2)
    bits = 0
    numbers = []
    if packet[6] == '0':
        length = packet[7:22]
        while bits < int(length, 2):
            index, num = process(packet[22+bits:])
            bits += index
            numbers.append(num)
        bits += 22
    elif packet[6] == '1':
        length = packet[7:18]
        bits = 0
        for _ in range(0, int(length,2)):
            index, num = process(packet[18+bits:])
            bits += index
            numbers.append(num)
        bits += 18
    result = 0
    if idtype == '000':
        for x in numbers:
            result += x
    elif idtype == '001':
        result = 1
        for x in numbers:
            result *= x
    elif idtype == '010':
        result = min(numbers)
    elif idtype == '011':
        result = max(numbers)
    elif idtype == '101':
        if numbers[0] > numbers[1]:
            result = 1
        else:
            result = 0
    elif idtype == '110':
        if numbers[0] < numbers[1]:
            result = 1
        else:
            result = 0
    elif idtype == '111':
        if numbers[0] == numbers[1]:
            result = 1
        else:
            result = 0
    return bits, result

print(process(data))



