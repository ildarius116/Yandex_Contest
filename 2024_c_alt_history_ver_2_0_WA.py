"""
C. Альтернативная история

Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Профессор математики Ерёменко разработал теорию, согласно которой реальных цивилизаций гораздо меньше, чем считают историки. В его теории есть основная цивилизация AA про которую известна последовательнось из NN исторических событий. Каждое событие обозначается числами от 11 до NN, каждое число встречается ровно один раз. В ii-й год в цивилизации происходило событие AiAi.
Кроме цивилизации AA существовали также две ”ложные” цивилизации BB и CC, для них профессор Ерёменко также выписал случившиеся с ними исторические события, происходившие синхронно с событиями в цивилизации AA. В ii-й год в цивилизации BB происходило событие BiBi, а в цивилизации CC — событие CiCi. Эти события также обозначены числами от 11 до NN (однако для этих цивилизаций числа могут повторяться).
В теории профессора Ерёменко порядок событий не важен, главное чтобы у всёх трех цивилизаций AA, BB и CC множества событий совпадали. Помогите профессору Ерёменко вычеркнуть информацию за некоторые годы (т.е. удалить из последовательностей элементы AiAi, BiBi, CiCi для некоторых ii) так, чтобы множества событий стали совпадать. Чтобы сенсационность открытия профессора была выше, необходимо минимизировать количество вычеркнутых годов.
Формат ввода
В первой строке задается число NN (1≤N≤1000001≤N≤100000) — количество событий для каждой из цивилизаций.
В следующих трёх строках задаются описания исторических событий, случившиеся с цивилизациями AA, BB и CC соответственно. Все последовательности имеют длину NN и состоят из чисел от 1 до NN. В последовательности AA все числа различны.
Формат вывода
Выведите одно число — минимальное количество лет, информацию о которых необходимо вычеркнуть.

Пример 1
Ввод
7
7 6 1 2 3 4 5
7 4 3 1 1 5 5
2 6 5 4 1 7 3
Вывод
4

Пример 2
Ввод
9
7 4 2 6 8 9 5 3 1
7 4 3 9 4 6 5 1 2
7 8 2 6 8 9 1 5 3
Вывод
2

Примечания
В первом примере необходимо удалить информацию за 1, 2, 4 и 6 годы (при нумерации с единицы). Тогда в каждой цивилизации останется множество событий [1,3,5][1,3,5]
Во втором примере необходимо удалить информацию за 2 и 5 годы (при нумерации с единицы). Тогда в каждой цивилизации останется множество событий [1,2,3,5,6,7,9][1,2,3,5,6,7,9]

"""
import itertools
from copy import deepcopy

N = int(input())
civ_a = list(map(int, input().split()))
civ_b = list(map(int, input().split()))
civ_c = list(map(int, input().split()))
civs_list = [civ_a, civ_b, civ_c]
civs_set_list = [set(civ_a), list(set(civ_b)), list(set(civ_c))]

count = 0
multy_event_list = []
event_dict = {1: {}, 2: {}}
for i, civ_list in enumerate((civ_b, civ_c)):
    for j, event in enumerate(civ_list):
        if event not in event_dict[i + 1]:
            event_dict[i + 1][event] = {'count': 0, 'poses': []}
        event_dict[i + 1][event]['count'] += 1
        event_dict[i + 1][event]['poses'].append(j)

multy_event_set = set()
multy_event_list = []
for key_i, item_i in event_dict.items():
    for key_j, item_j in item_i.items():
        if item_j['count'] > 1:
            multy_event_list.append(tuple(item_j['poses']))
multy_event_set = set(multy_event_list)
comb_event_list = []
if len(multy_event_set) > 1:
    tmp_comb_event_list = itertools.combinations(multy_event_set, len(multy_event_set))
    for comb_i in multy_event_list[0]:
        for comb_j in multy_event_list[1]:
            if comb_i != comb_j:
                tmp_comb = list(itertools.combinations((comb_i, comb_j), len(multy_event_list)))
                comb_event_list.append(tmp_comb[0])
    multy_event_list = comb_event_list
result_list = []
for combination in multy_event_list:
    civs_list_copy = deepcopy(civs_list)
    for civa in civs_list_copy:
        for i, ind in enumerate(combination):
            civa.pop(ind - i)
    if set(civs_list_copy[0]) == set(civs_list_copy[1]) == set(civs_list_copy[2]):
        result_list = civs_list_copy
    else:
        res_civs_list = deepcopy(civs_list_copy)
        sum_1 = sum(civs_list_copy[0])
        sum_2 = sum(civs_list_copy[1])
        sum_3 = sum(civs_list_copy[2])
        for i in range(1, len(civs_list_copy[0]) + 1):
            ind_combs_list = list(itertools.combinations(range(len(civs_list_copy[0])), i))
            for ind_combs in ind_combs_list:
                res_civs_list = deepcopy(civs_list_copy)
                for civa in res_civs_list:
                    for ind in ind_combs[::-1]:
                        civa.pop(ind)
                if res_civs_list[0] and set(res_civs_list[0]) == set(res_civs_list[1]) == set(res_civs_list[2]):
                    result_list = res_civs_list
                    break
count = N - len(result_list[0])
print(count)
