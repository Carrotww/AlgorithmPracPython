class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        import heapq

        flight_info = defaultdict(dict)
        for f in flights:
            flight_info[f[0]][f[1]] = f[2]

        queue = [(0, src, 0)]
        k_check = [n] * n

        while queue:
            curr_cost, curr_place, curr_k = heapq.heappop(queue)
            if curr_place == dst:
                return curr_cost

            if k_check[curr_place] >= curr_k:
                k_check[curr_place] = curr_k
                if curr_k <= k:
                    for next_place, next_cost in flight_info[curr_place].items():
                        heapq.heappush(queue, (curr_cost + next_cost, next_place, curr_k + 1))

        return -1
