def solution(n, times):
    result = 0
    left, right = min(times), max(times) * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for ti in times:
            cnt += mid // ti
            if cnt >= n:
                break
        if cnt >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

print(solution(6, [7, 10]))