import itertools
from collections import defaultdict
text = open('InputTxt/day19input.txt').read().strip()
scanners = text.split('\n\n')
beacons = []
for line in scanners:
    beacons_subset = []
    for character in line.split('\n'):
        if character.strip().startswith('--'):
            continue
        x,y,z = [int(w) for w in character.strip().split(',')]
        beacons_subset.append((x,y,z))
    beacons.append(beacons_subset)

def orientation(point, direction_bit):
    return_direction = [point[0], point[1], point[2]]
    for w, perm in enumerate(list(itertools.permutations([0, 1, 2]))):
        if direction_bit // 8 == w:
            return_direction = [return_direction[perm[0]], return_direction[perm[1]], return_direction[perm[2]]]

    if direction_bit % 2 == 1:
        return_direction[0] *= -1
    if (direction_bit // 2) % 2 == 1:
        return_direction[1] *= -1
    if (direction_bit // 4) % 2 == 1:
        return_direction[2] *= -1

    return return_direction

final = set(beacons[0])
points = [None for _ in range(len(beacons))]
points[0] = (0,0,0) ##origin

amount_of_beacons = set([0])
possibilities = set([x for x in range(1,len(beacons))])

adjustments = {}
for x in range(len(beacons)):
    for y in range(48):
        adjustments[(x,y)] = [orientation(point, y) for point in beacons[x]]

while possibilities:
    located = None
    for possibility in possibilities:
        if located:
            continue
        for z in [0]:
            scan = [tuple([p[0] + points[z][0], p[1] + points[z][1], p[2] + points[z][2]]) for p in final]

            for direction in range(48):
                d_scan = adjustments[(possibility, direction)]
                dictionary_x = defaultdict(int)
                for xc in range(len(beacons[possibility])):
                    for yc in range(len(scan)):
                        dx = -d_scan[xc][0] + scan[yc][0]
                        dy = -d_scan[xc][1] + scan[yc][1]
                        dz = -d_scan[xc][2] + scan[yc][2]
                        dictionary_x[(dx, dy, dz)] += 1
            for (dx,dy,dz), val in dictionary_x.items():
                if val >= 12:
                    points[possibility] = (dx, dy, dz)
                    for p in d_scan:
                        final.add(tuple([p[0] + dx, p[1] + dy, p[2] + dz]))
                    located = possibility
    possibilities.remove(located)
    amount_of_beacons.add(located)
print(len(final))

answer = 0
for p1 in points:
    for p2 in points:
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p1[2])
        if distance > answer:
            answer = distance
print(answer)





