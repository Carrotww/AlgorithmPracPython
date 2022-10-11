def solution(bridge_length, weight, truck_weights):
    def sum_list(_list):
        result = [0, 0]
        for _l in _list:
            result[0] += _l[0]
            result[1] += _l[1]
        return result

    from collections import deque

    curr_time = 0
    bridge = deque()
    truck_weights = deque(truck_weights)

    while True:
        if not bridge and not truck_weights:
            break

        if bridge and bridge[0][1] <= curr_time:
            bridge.popleft()

        if truck_weights and sum_list(bridge)[0] + truck_weights[0] <= weight:
            bridge.append([truck_weights.popleft(), curr_time + bridge_length])

        curr_time += 1
    return curr_time