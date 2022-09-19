# KCM Travel
import sys
import heapq
from collections import defaultdict

sys_input = sys.stdin.readline
INF = float('inf')


def main():
    # 테스트 케이스 입력 받기
    for _ in range(int(sys_input())):
        airport_num, support_price, num_of_tickets = map(int, sys_input().split())

        # dynamic table, 열은 공항을 의미, 행은 비용을 의미
        # dynamic table에 저장되는 값은 총 비행 시간
        dp = [[INF] * (airport_num + 1) for _ in range(support_price + 1)]
        graph = defaultdict(list)

        # k개의 input만큼 정보를 받아 graph를 채운다.
        for _ in range(num_of_tickets):
            depart_airport, arrival_airport, flight_cost, flight_time = map(int, sys_input().split())
            graph[depart_airport].append((arrival_airport, flight_cost, flight_time))

        # heap에 들어가는 순서는 거리, 비용, 공항
        heap = [(0, 0, 1)]
        while heap:
            curr_flight_time, curr_cost, curr_airport = heapq.heappop(heap)

            # 만약에 현재 거리가 dp에 저장된 값보다 크면,
            # 다시 말해 가장 빨리 도착하는 경로가 아닌 경우 스킵
            if curr_flight_time > dp[curr_cost][curr_airport]:
                continue
            dp[curr_cost][curr_airport] = curr_flight_time

            # heap에서 빼낸 curr_dist가 dp에 저장되어 있는 값보다 작거나 같으면 아래 알고리즘 수행
            # graph에 저장되어 있는 다음 공항, 티켓 비용, 이동시간을 받아옴
            for next_airport, next_cost, next_flight_time in graph[curr_airport]:
                total_time = curr_flight_time + next_flight_time
                total_cost = curr_cost + next_cost

                # 다음 공항까지 소모하는 비용이 지원금보다 작고, 이동시간이 최고 지원금이 total cost인 상태에서 해당 공항 까지
                # 도착할 때 까지의 이동 시간 보다 작을 때만 heap에 추가
                if total_cost <= support_price and total_time < dp[total_cost][next_airport]:
                    # 다음 공항까지 소모하는 비용부터 지원금까지 1원씩 증가시키며 dp값 갱신
                    for possible_cost in range(total_cost, support_price + 1):
                        if dp[possible_cost][next_airport] > total_time:
                            dp[possible_cost][next_airport] = total_time
                        else:
                            break
                    heapq.heappush(heap, (total_time, total_cost, next_airport))

        print(dp[support_price][airport_num] if dp[support_price][airport_num] != INF else "Poor KCM")


main()


# import sys
# import math
# from collections import defaultdict
#
#
# def solve():
#     for _ in range(int(sys.stdin.readline())):
#         n, m, k = map(int, sys.stdin.readline().rstrip().split())
#         table = defaultdict(list)
#         for _ in range(k):
#             u, v, c, d = map(int, sys.stdin.readline().rstrip().split())
#             table[u].append((v, c, d))
#
#         dp = [[math.inf] * (m+1) for _ in range(n + 1)]
#         dp[1][0] = 0
#
#         for money in range(m + 1):
#             for airport in range(1, n + 1):
#                 if dp[airport][money] != math.inf:
#                     for v, c, d in table[airport]:
#                         if money + c <= m:
#                             dp[v][money + c] = min(dp[v][money + c], dp[airport][money] + d)
#
#         result = min(dp[n])
#         print(result if result != math.inf else "Poor KCM")
#
#
# solve()
