"""
Ввод
2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964

Вывод
710 64F
710 64F
710 64f
"""


def syms_in_fio(fio):
    fio_set = set(''.join(fio))
    return len(fio_set)


def digs_in_bd(bd):
    digs_sum = 0
    for num in bd[:2]:
        digs_sum += sum(map(int, num))
    return digs_sum


results = []
N = int(input())
for i in range(N):
    data = input().split(',')
    fio = data[:3]
    bd = data[3:]
    letters_in_fio = syms_in_fio(fio)
    digs_sum = digs_in_bd(bd)
    frst_lttr_num = ord(fio[0][0].lower()) - ord('a') + 1
    result = letters_in_fio + digs_sum * 64 + frst_lttr_num * 256
    result = hex(result)[-3:].upper()
    results.append(result)
print(' '.join(results))
