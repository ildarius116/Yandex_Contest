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
