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

def intersection(x1, x2, x3, x4):
    return x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4

def get_intersection(x1, x2, x3, x4):
    if x3 < x1:
        return_x = x1
    else:
        return_x = x3

    if x4 < x2:
        return_y = x4
    else:
        return_y = x2

    return return_x, return_y

class Cube:

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.off = []

    def intersecting(self, adjacent):
        return intersection(self.x1, self.x2, adjacent.x1, adjacent.x2) and intersection(self.y1, self.y2, adjacent.y1, adjacent.y2) and intersection(self.z1, self.z2, adjacent.z1, adjacent.z2)

    def subtraction(self, adjacent):
        if self.intersecting(adjacent):
            x = get_intersection(self.x1, self.x2, adjacent.x1, adjacent.x2)
            y = get_intersection(self.y1, self.y2, adjacent.y1, adjacent.y2)
            z = get_intersection(self.z1, self.z2, adjacent.z1, adjacent.z2)

            for w in self.off:
                w.subtraction(adjacent)
            self.off.append(Cube(x[0], x[1], y[0], y[1], z[0], z[1]))

    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1) - sum([c.volume() for c in self.off])

text_two = open('InputTxt/day22input.txt').read().split('\n')
cubes_x = []
for line in text_two:
    (x1, x2, y1, y2, z1, z2) = tuple(map(int, re.findall(r'-?\d+', line)))

    cube = Cube(x1, x2, y1, y2, z1, z2)
    for c in cubes_x:
        c.subtraction(cube)
    if 'on' in line:
        cubes_x.append(cube)
print(sum([c.volume() for c in cubes_x]))



