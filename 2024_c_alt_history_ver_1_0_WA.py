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
N = input()
civ_a = sorted(list(map(int, input().split())))
civ_b = sorted(list(map(int, input().split())))
civ_c = sorted(list(map(int, input().split())))
civs_list = [civ_a, civ_b, civ_c]
civs_set_list = [set(civ_a), list(set(civ_b)), list(set(civ_c))]
inter_civ = set.intersection(set(civ_a), set(civ_b), set(civ_c), )
dif_civ_a = set(civ_a).difference(inter_civ)

multy_event_list = []
for event in set(civ_b):
    qty = civ_b.count(event)
    if qty > 1:
        multy_event_list.append(event)
for event in set(civ_c):
    qty = civ_c.count(event)
    if qty > 1:
        multy_event_list.append(event)
count = len(dif_civ_a)
for event in multy_event_list:
    if event not in dif_civ_a:
        count += 1
print(count)
