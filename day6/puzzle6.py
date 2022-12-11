with open('input1', 'r') as input_data:
    instructions = input_data.readlines()

#lights = [[False for i in range(1000)] for j in range(1000)]
lights = [[0 for i in range(1000)] for j in range(1000)]

for instruction in instructions:
    if instruction.startswith('turn'):
        _, do, start, _, end = instruction.strip().split()
    elif instruction.startswith('toggle'):
        do, start, _, end = instruction.strip().split()
    row_start, index_start = start.split(',')
    row_end, index_end = end.split(',')
    for i in range(int(row_start), int(row_end) + 1):
        for j in range(int(index_start), int(index_end) + 1):
            if do == 'on':
                #lights[i][j] = True
                lights[i][j] += 1
            elif do == 'off':
                #lights[i][j] = False
                if lights[i][j] > 0:
                    lights[i][j] -= 1
            elif do == 'toggle':
                #lights[i][j] = not lights[i][j]
                lights[i][j] += 2
#on = 0
brightness = 0
for i in lights:
    #on += i.count(True)
    brightness += sum(i)
#print(on)
print(brightness)
