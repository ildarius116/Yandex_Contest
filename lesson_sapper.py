import random


def make_field(X, Y, mines):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    field = []
    for i in range(Y + 2):
        field.append([0] * (X + 2))
    for mine_x, mine_y in mines:
        for i in range(len(dx)):
            field[mine_x + dx[i]][mine_y + dy[i]] += 1
    for mine_x, mine_y in mines:
        field[mine_x][mine_y] = '*'
    return field


mines = []
X, Y, M = 8, 8, 10
for _ in range(10):
    mines.append((random.randint(1, X), random.randint(1, Y)))
print(mines)
field = make_field(X, Y, mines)
for mine_line in field[1:-1]:
    print(*mine_line[1:-1])
