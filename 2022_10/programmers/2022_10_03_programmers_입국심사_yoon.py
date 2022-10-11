def solution(n, times):
    left = min(times)
    right = max(times) * n

    while right - left > 1:
        mid = (right + left) // 2
        check_sum = 0
        for t in times:
            check_sum += (mid // t)
        if check_sum >= n:
            right = mid
        else:
            left = mid

    return right
