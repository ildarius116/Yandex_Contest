import random


def apartment(K1, M, K2, P2, N2):
    if M >= N2:
        floor_sum_K2 = M * (P2 - 1) + N2
        aps_on_floor = (K2 // floor_sum_K2) + (1 if K2 % floor_sum_K2 > 0 else 0)
        if aps_on_floor and ((floor_sum_K2 - 1) * aps_on_floor <= K2) and (K2 <= floor_sum_K2 * aps_on_floor):
            floor_sum_K1 = (K1 // aps_on_floor) + (1 if K1 % aps_on_floor > 0 else 0)
            P1 = (floor_sum_K1 // M) + (1 if floor_sum_K1 % M > 0 else 0)
            aps_in_ent_to_K1 = (K1 - (P1 - 1) * aps_on_floor * M)
            N1 = (aps_in_ent_to_K1 // aps_on_floor) + (1 if (aps_in_ent_to_K1 % aps_on_floor) > 0 else 0)
            return P1, N1
    return -1, -1


max_app = 1000
max_ent = 20
max_floor = 9
cycles = 10
while cycles > 0:
    rand = [random.randint(1, max_app),
            random.randint(1, max_floor),
            random.randint(1, max_app),
            random.randint(1, max_ent),
            random.randint(1, max_floor)]
    res = apartment(*rand)
    print("Кв1: {}, Эт.Д: {},Кв2: {}, Под2: {}, Эт2: {} -> {}".format(*rand, res))
    cycles -= 1

# x = [3, 1, 7, 9, 3]
# print(appartment(*x))
K1 = 72
K2 = 74
P2 = 3
N2 = 1
M = 9
print(apartment(K1, M, K2, P2, N2))
K1 = 73
print(apartment(K1, M, K2, P2, N2))
K1 = 74
print(apartment(K1, M, K2, P2, N2))
K1 = 75
print(apartment(K1, M, K2, P2, N2))
K1 = 76
print(apartment(K1, M, K2, P2, N2))
K1 = 77
print(apartment(K1, M, K2, P2, N2))
K1 = 104
print(apartment(K1, M, K2, P2, N2))
K1 = 105
print(apartment(K1, M, K2, P2, N2))
# K1 = 106
# print(appartment(K1, K2, P2, N2, M))
# K1 = 107
# print(appartment(K1, K2, P2, N2, M))
# K1 = 108
# print(appartment(K1, K2, P2, N2, M))
# K1 = 109
# print(appartment(K1, K2, P2, N2, M))
# K1 = 110
# print(appartment(K1, K2, P2, N2, M))
# K1 = 111
# print(appartment(K1, K2, P2, N2, M))
# K1 = 112
# print(appartment(K1, K2, P2, N2, M))
# K1 = 99999
# print(appartment(K1, K2, P2, N2, M))
