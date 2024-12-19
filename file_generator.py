import random


pattern_order = []
pattern_ask = []
start = 1
end = 0
N = 200000
Q = 200000
with open('input.txt', 'w+') as file:
    file.write(str(N))
    file.write('\n')
    for _ in range(N):
        while True:
            start = random.randrange(1, 1000)
            end = random.randrange(1, 1000)
            if start < end:
                break
        cost = random.randrange(1, 1000)
        file.write(' '.join([str(start), str(end), str(cost)]))
        file.write('\n')

    file.write(str(Q))
    file.write('\n')

    for _ in range(Q):
        while True:
            start = random.randrange(1, 1000)
            end = random.randrange(1, 1000)
            if start < end:
                break
        type = random.randint(1, 2)
        file.write(' '.join([str(start), str(end), str(type)]))
        file.write('\n')



