import sys
import math

def solution():
    n, total_cost, tickets = map(int, sys.stdin.readline().split())
    path = [[] for _ in range(n + 1)]
    for _ in range(tickets):
        start, end, cost, time = map(int, sys.stdin.readline().split())
        path[start].append((end, cost, time))
    MAX = math.inf
    temp = [[MAX] * (total_cost + 1) for _ in range(n + 1)]
    temp[1][0] = 0

    for cost in range(total_cost + 1):
        for node in range(n + 1):
            if temp[node][cost] != MAX:
                for next_node, next_cost, next_time in path[node]:
                    if next_cost + cost <= total_cost:
                        temp[next_node][next_cost + cost] = min(temp[next_node][next_cost + cost], temp[node][cost] + next_time)
    
    result = min(temp[n])
    if result == MAX:
        print('Poor KCM')
    else:
        print(result)
        
T = int(input())
for _ in range(T):
    solution()


print(solution(3, 100, [[1, 2, 1, 1], [2, 3, 1, 1], [1, 3, 3, 30]]))
print(solution(4, 10, [[1, 2, 5, 3], [2, 3, 5, 4], [3, 4, 1, 5], [1, 3, 10, 6]]))
# import heapq

# def solution(n, total_cost, tickets):
#     pq = [(0, 0, 1)] # time, cost, node
#     path = [[] for _ in range(n + 1)]
#     for start, end, cost, time in tickets:
#         path[start].append((end, cost, time))
#     visited = {}
    
#     while pq:
#         cost, time, node = heapq.heappop(pq)
#         if node == n:
#             return time
#         if cost < total_cost and node not in visited:
#             visited[node] = time
#             for next_node, next_cost, next_time in path[node]:
#                 heapq.heappush(pq, (cost + next_cost, time + next_time, next_node))

#     return 'Poor KCM'

# T = int(input())
# for i in range(T):
#     temp = list(map(int, input().split()))
#     N, M = temp[0], temp[1]
#     tickets = []
#     for i in range(temp[2]):
#         ticket_info = list(map(int, input().split()))
#         tickets.append(ticket_info)
#     print(solution(N, M, tickets))

# print(solution(3, 100, [[1, 2, 1, 1], [2, 3, 1, 1], [1, 3, 3, 30]]))
# print(solution(4, 10, [[1, 2, 5, 3], [2, 3, 5, 4], [3, 4, 1, 5], [1, 3, 10, 6]]))