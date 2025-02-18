import math

n, m, x, y = map(int, input().split())
total_windows = x * y
threshold = math.ceil(total_windows / 2)
awake_apartments = 0
windows = [input().strip() for _ in range(n * x)]

for floor in range(n):
    for apartment in range(m):
        count_X = 0
        for h in range(x):
            window_row = windows[floor * x + h]
            count_X += window_row[apartment * y: apartment * y + y].count('X')
        if count_X >= threshold:
            awake_apartments += 1

print(awake_apartments)
