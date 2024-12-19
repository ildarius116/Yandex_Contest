def foo(pass_num, side, pos):
    seats = 'ABC_DEF'
    pattern = '.' * pass_num
    for key, value in row_dict.items():
        row_dict[key] = value.replace('X', '#')
        left, right = value.split('_')
        if side == 'left':
            if pos == 'aisle':
                if left.endswith(pattern):
                    ind = left.rfind(pattern)
                    text = f'Passengers can take seats:'
                    letters = seats[ind: ind + pass_num]
                    for letter in letters:
                        text += f' {key}{letter}'
                    rep = pattern.replace('.', 'X')
                    print(text)
                    left = rep.join(left.rsplit(pattern, 1))
                    row_dict[key] = left + '_' + right
                    for key, value in row_dict.items():
                        print(value)
                    return True
            else:
                if left.startswith(pattern):
                    ind = left.find(pattern)
                    text = f'Passengers can take seats:'
                    letters = seats[ind: ind + pass_num]
                    for letter in letters:
                        text += f' {key}{letter}'
                    rep = pattern.replace('.', 'X')
                    print(text)
                    left = left.replace(pattern, rep)
                    row_dict[key] = left + '_' + right
                    for key, value in row_dict.items():
                        print(value)
                    return True
        else:
            if pos == 'aisle':
                if right.startswith(pattern):
                    ind = right.find(pattern)
                    text = f'Passengers can take seats:'
                    letters = seats[ind: ind + pass_num]
                    for letter in letters:
                        text += f' {key}{letter}'
                    rep = pattern.replace('.', 'X')
                    print(text)
                    right = right.replace(pattern, rep)
                    row_dict[key] = left + '_' + right
                    for key, value in row_dict.items():
                        print(value)
                    return True
            else:
                if value.endswith(pattern):
                    ind = value.rfind(pattern)
                    text = f'Passengers can take seats:'
                    letters = seats[ind: ind + pass_num]
                    for letter in letters:
                        text += f' {key}{letter}'
                    rep = pattern.replace('.', 'X')
                    print(text)
                    right = rep.join(right.rsplit(pattern, 1))
                    row_dict[key] = left + '_' + right
                    for key, value in row_dict.items():
                        print(value)
                    return True
    return False


# rows = int(input())
# row_dict = {}
# for i in range(rows):
#     row_dict[i + 1] = input()
#
# npg = int(input())
# pass_list = []
# for i in range(npg):
#     pass_list.append(input().split(' '))

print(4)
row_dict = {1: '..._.#.', 2: '.##_...', 3: '.#._.##', 4: '..._...'}
for value in row_dict.values():
    print(value)
print(7)
pass_list = ['2 left aisle', '3 right window', '2 left window', '3 left aisle', '1 right window', '2 right window',
             '1 right window']
pass_list = list(map(lambda x: x.split(' '), pass_list.copy()))

for value in pass_list:
    print(value)

print('\nSTART\n')

for passengers in pass_list:
    pass_num = int(passengers[0])
    pattern = '.' * pass_num
    if not foo(int(passengers[0]), passengers[1], passengers[2]):
        print('Cannot fulfill passengers requirements')
