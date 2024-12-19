result_list = []
N = int(input())
orders_dict = {'order_start': {}, 'order_end': {}, }
for i in range(N):
    order_start, order_end, order_cost = map(int, input().split())
    if order_start not in orders_dict['order_start']:
        orders_dict['order_start'][order_start] = []
    orders_dict['order_start'][order_start].append((order_start, order_end, order_cost))
    if order_end not in orders_dict['order_end']:
        orders_dict['order_end'][order_end] = []
    orders_dict['order_end'][order_end].append((order_start, order_end, order_cost))
Q = int(input())
for _ in range(Q):
    ask_start, ask_end, ask_type = map(int, input().split())
    summary = 0
    for i in range(ask_start, ask_end + 1):
        if ask_type == 1:
            for order in orders_dict['order_start'].get(i, []):
                summary += order[2]
        elif ask_type == 2:
            for order in orders_dict['order_end'].get(i, []):
                summary += order[1] - order[0]
    result_list.append(str(summary))
print(' '.join(result_list))
