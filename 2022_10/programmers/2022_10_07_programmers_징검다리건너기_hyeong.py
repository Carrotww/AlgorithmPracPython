def solution(stones, k):
    left, right = 1, 200000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for st in stones:
            if st - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))