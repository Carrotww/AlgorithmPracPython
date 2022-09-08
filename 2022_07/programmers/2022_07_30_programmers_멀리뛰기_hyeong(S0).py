import math

def solution(n):
    def check(num):
        if num in memo:
            return memo[num]
        else:
            memo[num] = math.factorial(num)
            return memo[num]

    a = [x for x in range(n, -1, -2)]
    b = [x // 2 for x in range(0, n + 1, 2)]
    memo = {}
    result = 0
    for one, two in zip(a, b):
        result += check(one + two) // (check(one) * check(two))

    return result % 1234567