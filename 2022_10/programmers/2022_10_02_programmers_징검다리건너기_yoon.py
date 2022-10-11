# # 초기 효율성 테스트 통과하지 못한 풀이
# # 원인은 순차탐색을 이용하여 계속해서 max값을 갱신해야 할 때 문제 발생
#
#
# def solution(stones, k):
#     len_stones = len(stones)
#     max_val = max(stones[0: k])
#     result = max_val
#
#     for check_idx in range(0, len_stones - k):
#         if stones[check_idx] == max_val:
#             max_val = max(stones[check_idx + 1: check_idx + k + 1])
#             result = min(result, max_val)
#         if result == 1:
#             return result
#
#     return result

# 스터디 후 풀어본 이분 탐색을 이용한 풀이

def solution(stones, k):
    def is_pass(check_val):
        check_count = 0
        for s in stones:
            if s - check_val <= 0:
                check_count += 1
            else:
                check_count = 0
            if check_count == k:
                return False
        return True

    left = 1
    right = max(stones)

    while right - left > 1:
        mid = (left + right) // 2
        if is_pass(mid):
            left = mid
        else:
            right = mid

    return right

>>>>>>> b7ff3aec93ffbdfa4eb101f7866855d64758d18d
