import heapq

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]


def solution(n, paths, gates, summits):
    pq = [(0, gate) for gate in gates]
    MAX = 10000001
    min_dis = [MAX for _ in range(n + 1)]
    temp = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        temp[a].append((b, c))
        temp[b].append((a, c))
    summits = set(summits)

    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity
        if node in summits:
            continue
        for next_node, next_we in temp[node]:
            next_intensity = max(next_we, intensity)
            if min_dis[next_node] <= next_intensity:
                continue
            heapq.heappush(pq, (next_intensity, next_node))

    result = [0, MAX]

    for summit in summits:
        if min_dis[summit] < result[1]:
            result[0], result[1] = summit, min_dis[summit]
        elif min_dis[summit] == result[1] and summit < result[0]:
            result[0] = summit

    return result


print(solution(n, paths, gates, summits))
