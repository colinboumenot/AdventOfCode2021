import collections as c, re
text = open('InputTxt/day22input.txt').read().split('\n')

cubes = set()
for line in text:
    coordinate = list(map(int, re.findall(r'-?\d+', line)))
    if (coordinate[0] > 50 or coordinate[1] < -50 or coordinate[2] > 50 or coordinate[3] < -50 or coordinate[4] > 50 or coordinate[5] < -50):
        continue
    if 'on' in line:
        for x in range(max(coordinate[0], -50), min(50, coordinate[1]) + 1):
            for y in range(max(coordinate[2], -50), min(50, coordinate[3]) + 1):
                for z in range(max(coordinate[4], -50), min(50, coordinate[5]) + 1):
                    cubes.add((x,y,z))
    else:
        for x in range(max(coordinate[0], -50), min(50, coordinate[1]) + 1):
            for y in range(max(coordinate[2], -50), min(coordinate[3], 50) + 1):
                for z in range(max(coordinate[4], -50), min(coordinate[5], 50) + 1):
                    if (x,y,z) in cubes:
                        cubes.remove((x,y,z))

print(len(cubes))



