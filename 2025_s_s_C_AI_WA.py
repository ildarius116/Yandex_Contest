def process_taxi_orders(events):
    taxis = {}
    results = []
    for event in events:
        parts = event.split()
        event_type = parts[0]
        if event_type == "TAXI":
            timestamp = int(parts[1])
            taxi_id = int(parts[2])
            taxi_position = int(parts[3])
            taxis[taxi_id] = (timestamp, taxi_position)
        elif event_type == "ORDER":
            timestamp = int(parts[1])
            order_position = int(parts[3])
            order_time = int(parts[4])
            possible_taxis = []
            for taxi_id, (taxi_timestamp, taxi_position) in taxis.items():
                if taxi_timestamp <= timestamp:
                    max_distance = order_time * S
                    start_position = taxi_position
                    end_position = (taxi_position + max_distance) % L
                    if start_position <= end_position:
                        if start_position <= order_position <= end_position:
                            possible_taxis.append(taxi_id)
                    else:
                        if order_position >= start_position or order_position <= end_position:
                            possible_taxis.append(taxi_id)
            if possible_taxis:
                results.append(" ".join(map(str, possible_taxis[:5])))
            else:
                results.append("-1")

    return results


N, L, S = map(int, input().strip().split())
events = []
for i in range(N):
    events.append(input())
output = process_taxi_orders(events)
for line in output:
    print(line)
