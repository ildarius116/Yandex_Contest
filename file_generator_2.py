import random


civ_b = []
civ_c = []
N = 100
civ_a = list(map(str, range(1, N + 1)))

i = 1
while i <= N + 1:
    civ_b_num = str(random.randrange(1, N+1))
    civ_b.append(civ_b_num)
    i += 1
i = 1

while i <= N + 1:
    civ_c_num = str(random.randrange(1, N+1))
    civ_c.append(civ_c_num)
    i += 1

with open('input.txt', 'w+') as file:
    file.write(str(N))
    file.write('\n')
    file.write(' '.join(civ_a))
    file.write('\n')
    file.write(' '.join(civ_b))
    file.write('\n')
    file.write(' '.join(civ_c))
    file.write('\n')



