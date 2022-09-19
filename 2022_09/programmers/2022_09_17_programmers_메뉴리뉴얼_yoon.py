# 파이썬 combination 구현 방식
# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     result = []
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     result.append(tuple(pool[i] for i in indices))
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return result
#         indices[i] += 1
#         for j in range(i + 1, r):
#             indices[j] = indices[j - 1] + 1
#         result.append(tuple(pool[i] for i in indices))
#
#
# print(combinations('ABCDE', 3))

# 내 풀이 다듬은 것
def solution(orders, course):
    from collections import defaultdict
    from itertools import combinations

    result = []

    for course_len in course:
        candidates = defaultdict(int)
        for order in orders:
            tmp_candidates = list(combinations(sorted(order), course_len))
            for tmp_course in tmp_candidates:
                candidates[''.join(tmp_course)] += 1

        if candidates:
            max_course_count = max(candidates.items(), key=lambda x: x[1])[1]
            if max_course_count <= 1:
                continue
            else:
                result.extend([course for course, count in candidates.items() if count == max_course_count])

    return sorted(result)


# Counter와 most common 사용한 방식
def solution(orders, course):
    from collections import Counter
    from itertools import combinations

    result = []
    for course_len in course:
        candidates = list()
        for order in orders:
            candidates.extend(list(combinations(sorted(order), course_len)))
        c_counter = Counter(candidates).most_common()
        result.extend([''.join(c_course) for c_course, c_count in c_counter if
                       c_count == c_counter[0][1] and c_counter[0][1] > 1])

    return sorted(result)
