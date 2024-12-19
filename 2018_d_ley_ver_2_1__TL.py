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
result_list = []
N = int(input())
orders_dict = {0: {'cur_sum_cost': 0, 'cur_sum_time': 0}}
orders_events = []
max_event_time = 0
for i in range(N):
    order_start, order_end, order_cost = map(int, input().split())
    max_event_time = max(max_event_time, order_end)
    orders_events.append((order_start, order_end, -1, order_cost))
    orders_events.append((order_start, order_end, 1, order_cost))
orders_events.sort()

for event_time_st, event_time_end, ask_type, order_cost in orders_events:
    if ask_type == -1:
        if event_time_st not in orders_dict:
            orders_dict[event_time_st] = {'cur_sum_cost': 0, 'cur_sum_time': 0}
        orders_dict[event_time_st]['cur_sum_cost'] += order_cost
    elif ask_type == 1:
        if event_time_end not in orders_dict:
            orders_dict[event_time_end] = {'cur_sum_cost': 0, 'cur_sum_time': 0}
        orders_dict[event_time_end]['cur_sum_time'] += event_time_end - event_time_st

Q = int(input())
for _ in range(Q):
    ask_start, ask_end, ask_type = map(int, input().split())
    summary = 0
    if ask_type == 1:
        i = ask_start
        while i <= ask_end:
            orders_data = orders_dict.get(i, [])
            if orders_data:
                summary += orders_data['cur_sum_cost']
            i += 1
    elif ask_type == 2:
        i = ask_start
        while i <= ask_end:
            orders_data = orders_dict.get(i, [])
            if orders_data:
                summary += orders_data['cur_sum_time']
            i += 1
    result_list.append(str(summary))
print(' '.join(result_list))
