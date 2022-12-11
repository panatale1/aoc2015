from copy import deepcopy

with open('input1', 'r') as input_data:
    instructions = input_data.readlines()

instructions = instructions[0].strip()
index = [0,0]
houses_visited = [[0,0]]
s = [0,0]
rs = [0,0]
next_houses_visited = [[0,0]]
for i in range(len(instructions)):
    if instructions[i] == '^':
        index[1] += 1
        if i % 2 == 0:
            s[1] += 1
        else:
            rs[1] += 1
    elif instructions[i] == 'v':
        index[1] -= 1
        if i % 2 == 0:
            s[1] -= 1
        else:
            rs[1] -= 1
    elif instructions[i] == '<':
        index[0] -= 1
        if i % 2 == 0:
            s[0] -= 1
        else:
            rs[0] -= 1
    elif instructions[i] == '>':
        index[0] += 1
        if i % 2 == 0:
            s[0] += 1
        else:
            rs[0] += 1
    if index not in houses_visited:
        houses_visited.append(deepcopy(index))
    if i % 2 == 0:
        if s not in next_houses_visited:
            next_houses_visited.append(deepcopy(s))
    else:
        if rs not in next_houses_visited:
            next_houses_visited.append(deepcopy(rs))
print(len(houses_visited))
print(len(next_houses_visited))
