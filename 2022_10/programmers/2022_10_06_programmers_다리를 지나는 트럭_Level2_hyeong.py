from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_length = deque([0] * bridge_length)
    queue = deque(truck_weights)
    time = 0
    total_sum = 0
    while queue:
        if total_sum + queue[0] <= weight:
            left = total_length.popleft()
            right = queue.popleft()
            total_length.append(right)
            total_sum += right - left
            time += 1
        else:
            temp = total_length.popleft()
            total_sum -= temp
            if total_sum + queue[0] <= weight:
                left = queue.popleft()
                total_length.append(left)
                total_sum += left
            else:
                total_length.append(0)
            time += 1

    return time + len(total_length)

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))