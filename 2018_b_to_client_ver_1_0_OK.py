"""
Ввод
8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B

16
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B
50 7 25 2123722 A
14 23 52 36322 S
15 0 5 2123722 C
14 21 30 36322 A
50 7 26 2123722 C
14 21 30 2123722 A
14 21 40 36322 B
14 23 52 2123722 B

8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B
450 7 25 3632 A
414 23 52 212372 S
415 0 5 3632 C
414 21 30 212372 A
450 7 26 3632 C
414 21 30 3632 A
414 21 40 212372 B
414 23 52 3632 B
450 7 25 3632 A
414 23 52 212372 S
415 0 5 3632 C
414 21 30 212372 A
450 7 26 3632 C
414 21 30 3632 A
414 21 40 212372 B
414 23 52 3632 B

12
1 23 52 212375 S
1 21 40 212375 A
1 21 50 212375 B
366 1 52 212375 S
365 21 40 212375 A
365 21 50 212375 B
65 23 52 212375 S
65 21 40 212375 A
65 21 50 212375 B
465 23 52 212375 S
465 21 40 212375 A
465 21 50 212375 B

264
396
Вывод
156 142

"""
import collections


def time_to_minutes(time):
    to_int = list(map(int, time))
    total_minutes = to_int[0] * 1440 + to_int[1] * 60 + to_int[2]
    return total_minutes


rockets_dict = {}
result_dict = {}
N = int(input())
for _ in range(N):
    data = input().split()
    status = data[4]
    data = list(map(int, data[:4]))
    data.append(status)
    if data[3] not in rockets_dict:
        rockets_dict[data[3]] = []
    rockets_dict[data[3]].append(data)
for key in rockets_dict.keys():
    sum_time_for_year = 0
    sum_time_for_trip = 0
    start_for_trip = 0
    take_for_trip = 0
    is_dep = False
    next_year = False
    rockets_dict[key] = sorted(rockets_dict[key])
    for event in rockets_dict[key]:
        if not next_year:
            year = int(event[0])
            if year <= 365:
                if event[4] == 'A':
                    start_for_trip = time_to_minutes(event[0:3])
                    sum_time_for_trip = 0
                elif event[4] == 'B':
                    is_dep = True
                    take_for_trip = time_to_minutes(event[0:3])
                    sum_time_for_trip = take_for_trip - start_for_trip
                elif event[4] == 'C':
                    cancel = time_to_minutes(event[0:3])
                    if is_dep:
                        sum_time_for_trip += cancel - take_for_trip
                    else:
                        sum_time_for_trip += cancel - start_for_trip
                    sum_time_for_year += sum_time_for_trip
                    is_dep = False
                elif event[4] == 'S':
                    arrive = time_to_minutes(event[0:3])
                    sum_time_for_trip += arrive - take_for_trip
                    sum_time_for_year += sum_time_for_trip
                    is_dep = False
            else:
                start_for_trip = 0
                next_year = True
    result_dict[int(key)] = str(sum_time_for_year)
result_dict = collections.OrderedDict(result_dict, )
result_list = sorted(result_dict.items(), key=lambda x: x[0])
# print(result_list)
print(' '.join(x[1] for x in result_list))
