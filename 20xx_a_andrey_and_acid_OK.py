def foo(arr):
    a_max = max(arr)
    if a_max != arr[-1]:
        return -1
    prev = 0
    a_min = a_max
    for ai in arr:
        if ai < prev:
            return -1
        prev = ai
        if ai < a_min:
            a_min = ai
    return a_max - a_min


n = int(input())
a = (input())
array = list(map(lambda x: int(x), (a.split(' '))))
print(foo(array))
