with open('input1', 'r') as input_data:
    directions = input_data.readlines()

if len(directions) == 1:
    directions = directions[0].strip()

basement = False
basement_index = 0
floor = 0
for i in range(len(directions)):
    if directions[i] == '(':
        floor += 1
    else:
        floor -= 1
        if floor == -1 and not basement:
            basement_index = i + 1
            basement = True
print(floor)
print(basement_index)
