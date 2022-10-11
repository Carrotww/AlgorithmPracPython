# 개똥벌레가 석순과 종유석을 파괴하며 나아감
# 시작은 석순 끝은 종유석
# 동굴 길이 항상 짝수 (N: 2이상 200,000이하)
# 동굴 높이 2이상 500,000이하
# 처음 입력으로 N과 H가 주어지며 N개 줄에 장애물 크기 순서대로 주어짐

# 내가 푼 풀이 : 통과
# def solution():
#     import sys
#
#     sys_input = sys.stdin.readline
#
#     n, h = map(int, sys_input().strip().split())
#
#     b_obstacle_list = [0 for _ in range(h + 1)]
#     t_obstacle_list = [0 for _ in range(h + 1)]
#     for i in range(n):
#         if i % 2 == 0:
#             b_obstacle_list[int(sys_input().strip())] += 1
#         else:
#             t_obstacle_list[int(sys_input().strip())] += 1
#
#     for check_h in range(h, 1, -1):
#         b_obstacle_list[check_h - 1] += b_obstacle_list[check_h]
#         t_obstacle_list[check_h - 1] += t_obstacle_list[check_h]
#
#     min_val = n + 1
#     count = 0
#
#     for _h in range(1, h + 1):
#         tmp_min_val = b_obstacle_list[_h] + t_obstacle_list[h + 1 - _h]
#         if tmp_min_val < min_val:
#             min_val = tmp_min_val
#             count = 1
#         elif tmp_min_val == min_val:
#             count += 1
#
#     print(f'{min_val} {count}')


# 이분 탐색 이용한 풀이
def solution():
    def get_crash_num(flight_height, obstacle_list):
        left = 0
        right = len(obstacle_list) - 1

        while left <= right:
            mid = (left + right) // 2

            if obstacle_list[mid] <= flight_height:
                left = mid + 1
            else:
                right = mid - 1

        return len(obstacle_list) - (right + 1)

    import sys

    sys_input = sys.stdin.readline

    n, h = map(int, sys_input().strip().split())

    b_obstacle_list = list()
    t_obstacle_list = list()
    for i in range(n):
        if i % 2 == 0:
            b_obstacle_list.append(int(sys_input().strip()))
        else:
            t_obstacle_list.append(int(sys_input().strip()))

    b_obstacle_list.sort()
    t_obstacle_list.sort()

    min_val = n + 1
    count = 0

    for _h in range(1, h + 1):
        tmp_min_val = get_crash_num(h - _h, t_obstacle_list) + get_crash_num(_h - 1, b_obstacle_list)
        if tmp_min_val < min_val:
            min_val = tmp_min_val
            count = 1
        elif tmp_min_val == min_val:
            count += 1

    print(f'{min_val} {count}')


solution()
