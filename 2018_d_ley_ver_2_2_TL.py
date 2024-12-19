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
N = int(input())
result_list = []
orders_events = []
max_event_time = 0
for i in range(N):
    order_start, order_end, order_cost = map(int, input().split())
    max_event_time = max(max_event_time, order_end)
    orders_events.append((order_start, order_end, -1, order_cost))
    orders_events.append((order_start, order_end, 1, order_cost))

orders_list = []
for _ in range(max_event_time + 1):
    orders_list.append([0, 0])  # [cur_sum_cost, cur_sum_time]
sum_cost = sum_time = 0
prev_event_time_st = prev_event_time_end = 0
for event_time_st, event_time_end, ask_type, order_cost in orders_events:
    if ask_type == -1:
        orders_list[event_time_st][0] += order_cost
    elif ask_type == 1:
        orders_list[event_time_end][1] += event_time_end - event_time_st


def foo(*data):
    ask_start, ask_end, ask_type = data

    ask_list = orders_list[ask_start:ask_end + 1]
    summary = 0
    i = 0
    if ask_type == 1:
        while i < len(ask_list):
            data = ask_list[i]
            if data:
                summary += data[0]
            i += 1
    elif ask_type == 2:
        while i < len(ask_list):
            data = ask_list[i]
            if data:
                summary += data[1]
            i += 1
    result_list.append(str(summary))
    return result_list


Q = int(input())
for _ in range(Q):
    ask_start, ask_end, ask_type = map(int, input().split())
    result_list = foo(ask_start, ask_end, ask_type)
print(' '.join(result_list))
