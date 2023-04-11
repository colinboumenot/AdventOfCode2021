import ast

text = open('InputTxt/day18input.txt').read().strip().splitlines()
data = []
for line in text:
    data.append(ast.literal_eval(line))



def add(a, b):
    return reduce_([a,b])

def reduce_(string):
    explosion, chain = explode(string)
    if explosion:
        return reduce_(chain)
    else:
        explosion_two, chain_two = split_l(string)
        if explosion_two:
            return reduce_(chain_two)
        else:
            return chain_two

def split_l(string):
    if isinstance(string, list):
        occurred, chain = split_l(string[0])
        if occurred:
            return True, [chain, string[1]]
        else:
            occurred_two, chain_two = split_l(string[1])
            return occurred_two, [chain, chain_two]
    else:
        if string >= 10:
            return True, [(string // 2), ((string + 1) // 2)]
        else:
            return False, string

def explode(c):
    chain = str(c)
    new_chain = []
    index = 0
    while index < len(chain):
        if not chain[index].isdigit():
            if chain[index] != ' ':
                new_chain.append(chain[index])
            index += 1
        else:
            current = index
            while current < len(chain) and chain[current].isdigit():
                current += 1
            new_chain.append(int(chain[index:current]))
            index = current

    depth = 0
    for i, sub_chain in enumerate(new_chain):
        if sub_chain == '[':
            depth += 1
            if depth == 5:
                left = new_chain[i + 1]
                right = new_chain[i + 3]
                left_index = None
                right_index = None
                for z in range(len(new_chain)):
                    if isinstance(new_chain[z], int) and z < i:
                        left_index = z
                    elif isinstance(new_chain[z], int) and z > i + 3 and right_index is None:
                        right_index = z
                if right_index is not None:
                    new_chain[right_index] += right
                new_chain = new_chain[:i] + [0] + new_chain[i + 5:]
                if left_index is not None:
                    new_chain[left_index] += left
                return True, eval(''.join([str(line_2) for line_2 in new_chain]))
        elif sub_chain == ']':
            depth -= 1
        else:
            pass
    return False, c

def magnitude(string):
    if isinstance(string, list):
        return 3 * magnitude(string[0]) + 2 * magnitude(string[1])
    else:
        return string

total = data[0]
for line in data[1:]:
    total = add(total, line)
print(magnitude(total))

answer = None
for x in data:
    for y in data:
        if x != y:
            score = magnitude(add(x,y))
            if answer is None or score > answer:
                answer = score
print(answer)