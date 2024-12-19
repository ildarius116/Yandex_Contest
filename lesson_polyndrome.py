

def foo(arr):
    left_side = []
    right_side = []
    k = 0
    for j in range(len(arr) - 1, 1, -1):
        right_side.append(arr[j])
        for k in range(len(arr) - j - 1, len(arr)):
            left_side.append(arr[k])
            print(left_side, right_side)
            print('j:', j, 'k:', k)

            for m in range(len(left_side)):
                if left_side[m] != right_side[m]:
                    left_side.clear()
                    left_side.append(arr[k])
                    break
            if len(left_side) == len(right_side):
                if left_side == right_side:
                    break
                else:
                    left_side.clear()
        if k + 1 == j:
            break
    add_index = len(arr) - (len(right_side) * 2) - 1
    print(add_index)
    add_arr = arr[add_index::-1]
    print(add_arr)
    arr.extend(add_arr)
    return arr


x = [1, 2, 3, 4, 5, 4, 4, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1]
print(foo(x))



def foo2(arr):
    return arr


x = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1]
# print(foo2(x))
