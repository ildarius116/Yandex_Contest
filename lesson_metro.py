import timeit
def trains(a, b, lag, n, m):
    train_limit_1_min = (n - 1) * (lag + a) + lag
    train_limit_1_max = (n - 1) * (lag + a) + lag + 2 * a
    train_limit_2_min = (m - 1) * (lag + b) + lag
    train_limit_2_max = (m - 1) * (lag + b) + lag + 2 * b
    print('train_limit_1:', train_limit_1_min, train_limit_1_max)
    print('train_limit_2:', train_limit_2_min, train_limit_2_max)
    min_t = max(train_limit_1_min, train_limit_2_min)
    max_t = min(train_limit_1_max, train_limit_2_max)
    return (min_t, max_t) if min_t < max_t else False

start_pr = timeit.timeit()
print(start_pr)

a = 5
b = 7
lag = 1
n = 10
m = 6
print(trains(a, b, lag, n, m))
start_pr = timeit.timeit()
print(start_pr)
