from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # node -> n, route -> times
        pq = [(0, k)]
        MAX = 6001
        min_dis = [MAX for _ in range(n + 1)] # minimum distance initialize
        temp = [[] for _ in range(n + 1)]

        for start, end, weight in times:
            temp[start].append((end, weight))
        
        while pq:
            intensity, node = heapq.heappop(pq)
            if min_dis[node] <= intensity:
                continue
            min_dis[node] = intensity

            for next_node, next_val in temp[node]:
                heapq.heappush(pq, (next_val + intensity, next_node))
        
        result = 0
        
        for i in range(1, n + 1):
            if min_dis[i] == MAX:
                return -1
            result = max(result, min_dis[i])

        return result

test = Solution()
print(test.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(test.networkDelayTime([[1,2,1]], 2, 1))
print(test.networkDelayTime([[1,2,1]], 2, 2))
print(test.networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))