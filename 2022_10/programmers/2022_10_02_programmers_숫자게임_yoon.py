def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    b_idx = 0

    result = 0
    for a in A:
        if B[b_idx] > a:
            result += 1
            b_idx += 1

    return result
