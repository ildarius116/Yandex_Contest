result_list = []
N = int(input())
order_events = []
for i in range(N):
    order_start, order_end, order_cost = map(int, input().split())
    order_events.append((order_start, order_end, order_cost))
order_events = tuple(order_events)
Q = int(input())
ask_events = []
for j in range(Q):
    ask_start, ask_end, ask_type = map(int, input().split())
    sum_cost = sum_time = 0
    for i in range(N):
        order_start, order_end, order_cost = order_events[i]
        if ask_type == 1 and ask_start <= order_start <= ask_end:
            sum_cost += order_cost
        elif ask_type == 2 and ask_start <= order_end <= ask_end:
            sum_time += order_end - order_start
    if ask_type == 1:
        result_list.append(str(sum_cost))
    elif ask_type == 2:
        result_list.append(str(sum_time))

print(' '.join(result_list))
