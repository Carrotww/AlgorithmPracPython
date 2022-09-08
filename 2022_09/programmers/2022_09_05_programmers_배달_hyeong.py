import heapq

def solution(n, road, k): # n : number of node, k : max intensity
    pq = []
    pq.append((0, 1)) # intensity, node
    result = 0
    MAX = 20000001
    temp = [[] for _ in range(n + 1)] # Route - re
    for a, b, c in road:
        temp[a].append((b, c))
        temp[b].append((a, c))
    min_dis = [MAX for _ in range(n + 1)] # max distance for node

    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dis[node] < intensity:
            continue
        min_dis[node] = intensity
        for next_node, next_val in temp[node]:
            sum_intensity = intensity + next_val
            if min_dis[next_node] < sum_intensity:
                continue
            heapq.heappush(pq, (sum_intensity, next_node))

    for i in min_dis:
        if i <= k:
            result += 1

    return min_dis, result

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))