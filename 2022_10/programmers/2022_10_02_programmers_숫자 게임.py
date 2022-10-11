def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    b_index = 0
    for i in range(len(A)):
        if B[b_index] > A[i]:
            cnt += 1
            b_index += 1
    return cnt