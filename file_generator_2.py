import random

N = n = 100_000
# N = n = 9
civ_a = []
civ_b = []
civ_c = []
random_set = set()
random_list = []

while n > 0:
    random_num = random.randrange(1, N + 1)
    if str(random_num) not in random_set:
        print(n)
        random_list.append(str(random_num))
        n -= 1
        random_set = set(random_list)
# print(random_list)
print(len(random_list))

for num in random_list:
    random_chance = random.randrange(1, 10)
    random_pos = random.randrange(1, N)
    if random_chance == 1:
        civ_a.append(num)
        civ_b.append(num)
        civ_c.append(random_list[random_pos])
    elif random_chance == 2:
        civ_a.append(num)
        civ_b.append(random_list[random_pos])
        civ_c.append(num)
    elif random_chance == 3:
        civ_a.append(num)
        civ_b.append(num)
        civ_c.append(num)
    elif random_chance in range(4, 11):
        civ_a.append(num)
        civ_b.append(random_list[random_pos])
        civ_c.append(random_list[random_pos])

with open('input.txt', 'w+') as file:
    file.write(str(N))
    file.write('\n')
    file.write(' '.join(civ_a))
    file.write('\n')
    file.write(' '.join(civ_b))
    file.write('\n')
    file.write(' '.join(civ_c))
    file.write('\n')
