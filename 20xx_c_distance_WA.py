def foo(arr):
    for i in range(1, len(arr) + 1):
        print('i:', i)

        if i == 1:
            s = [int(arr[1]), int(arr[2])]
            print('s:', s)
            dist = abs(i - s[0]) + abs(i - s[1])
            print(f'|{i}-{s[0]}| + |{i}-{s[1]}| = {dist}')

        elif i == len(arr):
            s = [int(arr[-3]), int(arr[-2])]
            dist = abs(i - s[0]) + abs(i - s[1])
            print(f'|{i}-{s[0]}| + |{i}-{s[1]}| = {dist}')
        else:
            s = [int(arr[i - 2]), int(arr[i])]
            dist = abs(i - s[0]) + abs(i - s[1])
            print(f'|{i}-{s[0]}| + |{i}-{s[1]}| = {dist}')

        # print(dist)
        # print(dist, end=' ')
    print()


# n, k = input('n k: ').split(' ')
# a_in = input('a: ').split(' ')
# foo(a_in)

input_list = [['4 2', '1 2 3 4'], ['5 3', '3 2 5 1 2'], ['6 2', '3 2 1 1 2 3']]
for item in input_list:
    n_k, a_in = item
    n, k = n_k.split(' ')
    a_in = a_in.split(' ')
    print('a_in:', a_in)
    foo(a_in)
