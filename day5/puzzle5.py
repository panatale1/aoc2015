with open('input1', 'r') as input_data:
    strings = input_data.readlines()

nice = 0
vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']
for i in strings:
    string = i.strip()
    has_forbidden = False
    for j in forbidden:
        if j in string:
            has_forbidden = True
            break
    if has_forbidden:
        continue
    vowel_count = 0
    for j in vowels:
        vowel_count += string.count(j)
    if vowel_count <3:
        continue
    has_pair = False
    for j in range(len(string) - 1):
        if string[j] == string[j + 1]:
            has_pair = True
            break
    if not has_pair:
        continue
    nice += 1
print(nice)

nice = 0
for i in strings:
    string = i.strip()
    has_repeating_pair = False
    for j in range(len(string) - 1):
        if string.count(string[j:j + 2]) > 1:
            has_repeating_pair = True
            break
    if not has_repeating_pair:
        continue
    has_set = False
    for j in range(len(string) - 2):
        if string[j] == string[j + 2]:
            has_set = True
            break
    if not has_set:
        continue
    nice += 1
print(nice)
