# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = [] # return 결과 값 저장
    for cnt in course:
        temp = defaultdict(int)
        for menu in orders:
            for com in combinations(sorted(menu), cnt):
                temp[com] += 1
        if temp.values():
            max_val = max(list(temp.values()))
        for menu, cnt in temp.items():
            if cnt == max_val and cnt != 1:
                result.append(''.join(menu))
    
    return list(sorted(result))