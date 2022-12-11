with open('input1', 'r') as input_data:
    gifts = input_data.readlines()

paper = 0
ribbon = 0
for i in gifts:
    gift = i.strip()
    lwh = gift.split('x')
    for j in range(3):
        lwh[j] = int(lwh[j])
    lwh.sort()
    paper += 2 * lwh[0] * lwh[1] + 2 * lwh[1] * lwh[2] + 2 * lwh[0] * lwh[2] + lwh[0] * lwh[1]
    ribbon += 2 * lwh[0] + 2 * lwh[1] + lwh[0] * lwh[1] * lwh[2]
print(paper)
print(ribbon)
