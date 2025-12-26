import time

start_pr = time.time()
print("start:", start_pr)

file = open('input.txt', 'r')
N = int(file.readline())

result_list = []

orders_dict = {'order_start': {}, 'order_end': {}, }
for i in range(N):
    # order_start, order_end, order_cost = map(int, input().split())
    order_start, order_end, order_cost = map(int, file.readline().strip().split())
    if order_start not in orders_dict['order_start']:
        orders_dict['order_start'][order_start] = []
    orders_dict['order_start'][order_start].append((order_start, order_end, order_cost))
    if order_end not in orders_dict['order_end']:
        orders_dict['order_end'][order_end] = []
    orders_dict['order_end'][order_end].append((order_start, order_end, order_cost))

print("medium:", time.time())

# Q = int(input())
Q = int(file.readline())
for _ in range(Q):
    # ask_start, ask_end, ask_type = map(int, input().split())
    ask_start, ask_end, ask_type = map(int, file.readline().strip().split())
    summary = 0
    for i in range(ask_start, ask_end + 1):
        if ask_type == 1:
            for order in orders_dict['order_start'].get(i, []):
                summary += order[2]
        elif ask_type == 2:
            for order in orders_dict['order_end'].get(i, []):
                summary += order[1] - order[0]
    result_list.append(str(summary))
# print(' '.join(result_list))

stop_pr = time.time()
print("stop:", stop_pr)
print("result:", stop_pr - start_pr)
