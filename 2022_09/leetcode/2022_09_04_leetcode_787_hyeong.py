import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = []
        pq.append((0, src, 0))
        temp = [[] for _ in range(n)]

        for a, b, c in flights:
            temp[a].append((b, c))

        visit = dict()

        while pq:
            intensity, node, cnt = heapq.heappop(pq)
            if node == dst:
                return intensity

            if node not in visit or cnt <= visit[node]:
                visit[node] = cnt
                for next_node, next_val in temp[node]:
                    current_intensity = intensity + next_val
                    if cnt > k:
                        continue
                    heapq.heappush(pq, (current_intensity, next_node, cnt + 1))

        return -1