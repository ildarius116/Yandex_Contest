"""
10
3 6 1
4 6 2
3 4 3
4 4 100500
4 11 777
3 8 365
4 8 31
5 20 5
6 21 4
6 22 3
6
6 6 2
6 8 2
5 9 2
3 12 2
9 12 2
8 12 2


"""
import time

start_pr = time.time()
print("start:", start_pr)

file = open('input.txt', 'r')
N = int(file.readline())
result_list = []
orders_dict = {0: {'prev_cost': 0, 'cur_cost': 0, 'sum_cost': 0, 'prev_time': 0, 'cur_time': 0, 'sum_time': 0}}
orders_events = []
max_event_time = 0
for i in range(N):
    order_start, order_end, order_cost = map(int, file.readline().strip().split())
    max_event_time = max(max_event_time, order_end)
    orders_events.append((order_start, order_end, -1, order_cost))
    orders_events.append((order_start, order_end, 1, order_cost))
orders_events.sort()

for event_time_st, event_time_end, ask_type, order_cost in orders_events:
    if ask_type == -1:
        if event_time_st not in orders_dict:
            orders_dict[event_time_st] = {'prev_cost': 0, 'cur_cost': 0, 'sum_cost': 0,
                                          'prev_time': 0, 'cur_time': 0, 'sum_time': 0}
        orders_dict[event_time_st]['cur_cost'] += order_cost
    elif ask_type == 1:
        if event_time_end not in orders_dict:
            orders_dict[event_time_end] = {'prev_cost': 0, 'cur_cost': 0, 'sum_cost': 0,
                                           'prev_time': 0, 'cur_time': 0, 'sum_time': 0}
        orders_dict[event_time_end]['cur_time'] += event_time_end - event_time_st
orders_events.clear()

orders_list = [0] * (max_event_time + 2)
prev_sum = prev_time = 0
sum_cost = sum_time = 0
orders_dict = dict(sorted(orders_dict.items()))
for key, item in orders_dict.items():
    orders_dict[key]['prev_cost'] = prev_sum
    prev_sum = orders_dict[key].get('cur_cost', 0)
    sum_cost += orders_dict[key].get('cur_cost', 0)
    orders_dict[key]['sum_cost'] = sum_cost
    orders_dict[key]['prev_time'] = prev_time
    prev_time = orders_dict[key].get('cur_time', 0)
    sum_time += orders_dict[key].get('cur_time', 0)
    orders_dict[key]['sum_time'] = sum_time
    orders_list[key] = key

print("medium:", time.time())

Q = int(file.readline())
for j in range(Q):
    ask_start, ask_end, ask_type = map(int, file.readline().strip().split())
    if ask_end >= len(orders_list):
        ask_end = len(orders_list) - 1
    orders_list_slice = orders_list[ask_start:ask_end + 1]
    search_min = search_max = i = 0
    s_min = s_max = False
    while i < len(orders_list_slice):
        orders_l_s = orders_list_slice[i]
        if not s_min and orders_l_s:
            search_min = orders_l_s
            s_min = True
        orders_l_s = orders_list_slice[len(orders_list_slice) - 1 - i]
        if not s_max and orders_l_s:
            search_max = orders_l_s
            s_max = True
        if s_min and s_max:
            break
        i += 1

    summary = 0
    if ask_type == 1 and search_min and search_max:
        summary = orders_dict[search_max].get('sum_cost', 0) - orders_dict[search_min].get('sum_cost', 0) + orders_dict[search_min].get('cur_cost', 0)
    elif ask_type == 2 and search_min and search_max:
        summary = orders_dict[search_max].get('sum_time', 0) - orders_dict[search_min].get('sum_time', 0) + orders_dict[search_min].get('cur_time', 0)
    result_list.append(str(summary))
# print(' '.join(result_list))
with open('output.txt', 'w+') as file:
    file.write(' '.join(result_list))

stop_pr = time.time()
print("stop:", stop_pr)
print("result:", stop_pr - start_pr)
