class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict, deque

        net_info = defaultdict(list)
        for source, target, time in times:
            net_info[source].append([target, time])

        visited = [-1] * n
        queue = deque([(k, 0)])

        while queue:
            curr_node, curr_time = queue.popleft()
            if visited[curr_node - 1] == -1 or visited[curr_node - 1] > curr_time:
                visited[curr_node - 1] = curr_time
                for next_node, trans_cost in net_info[curr_node]:
                    queue.append((next_node, curr_time + trans_cost))

        return -1 if -1 in visited else max(visited)

    # Heap Queue 이용 방식
    # class Solution:
    #     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #         from collections import defaultdict
    #         import heapq
    #
    #         network_info = defaultdict(list)
    #         for source, target, time in times:
    #             network_info[source].append([target, time])
    #
    #         visited = [-1] * n
    #         queue = [(0, k)]
    #
    #         while queue:
    #             curr_cost, curr_node = heapq.heappop(queue)
    #             if visited[curr_node - 1] == -1:
    #                 visited[curr_node - 1] = curr_cost
    #
    #                 for next_node, next_cost in network_info[curr_node]:
    #                     heapq.heappush(queue, (next_cost + curr_cost, next_node))
    #
    #         return -1 if -1 in visited else max(visited)
