def solution(N, road, K):
    from collections import defaultdict
    from collections import deque

    road_info = defaultdict(list)
    for town1, town2, move_cost in road:
        road_info[town1].append([town2, move_cost])
        road_info[town2].append([town1, move_cost])

    visited = [-1] * N
    queue = deque([(1, 0)])

    while queue:
        curr_place, curr_cost = queue.popleft()
        if visited[curr_place - 1] == -1 or curr_cost < visited[curr_place - 1]:
            visited[curr_place - 1] = curr_cost

            for next_place, next_cost in road_info[curr_place]:
                queue.append((next_place, curr_cost + next_cost))

    return len([town for town in visited if town != -1 and town <= K])

# Heap Queue 쓴 방식

# def solution(N, road, K):
#     import heapq
#     from collections import defaultdict
#
#     road_info = defaultdict(list)
#     for town1, town2, move_cost in road:
#         road_info[town1].append([town2, move_cost])
#         road_info[town2].append([town1, move_cost])
#
#     visited = [-1] * N
#     queue = [(0, 1)]
#
#     while queue:
#         curr_cost, curr_town = heapq.heappop(queue)
#         if visited[curr_town - 1] == -1:
#             visited[curr_town - 1] = curr_cost
#
#             for next_town, move_cost in road_info[curr_town]:
#                 if visited[next_town - 1] == -1:
#                     heapq.heappush(queue, (curr_cost + move_cost, next_town))
#
#     return len([town for town in visited if town <= K and town != -1])
