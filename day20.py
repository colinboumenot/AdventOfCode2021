from collections import defaultdict

text = open('InputTxt/day20input.txt')
algorithm, image = text.read().split('\n\n')
algorithm_grid = [str(int(x == '#')) for x in algorithm]
image = ([[str(int(y == '#')) for y in x] for x in image.split('\n')])
image_dictionary = defaultdict(lambda: '0')
image_dictionary.update({(i, j): image[i][j] for i in range(len(image)) for j in range(len(image[0]))})



def adjacent(x, y):
    for dx in range(x - 1, x + 2):
        for dy in range(y - 1, y + 2):
            yield (dx, dy)

def zoom(grid_dictionary, algorithm_x, steps = 2):
    for z in range(steps):
        m, M = -2 * steps, 100 + 2 * steps
        grid = defaultdict(lambda: str(z % 2))
        grid.update(grid_dictionary)
        grid_dictionary = {(i,j): algorithm_x[int(''.join(grid[(x, y)] for x, y in adjacent(i, j)), 2)] for i in range(m, M) for j in range(m, M)}
    return grid_dictionary

##counter = defaultdict(int)
##answer = zoom(image_dictionary, algorithm_grid)
##for value in answer.values():
    ##counter[value] += 1
##print(counter)

new_counter = defaultdict(int)
answer_two = zoom(image_dictionary, algorithm_grid, 50)
for value in answer_two.values():
    new_counter[value] += 1
print(new_counter)




