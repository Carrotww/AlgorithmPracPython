from collections import deque

def solution(people, limit):
    cnt = 0
    people = sorted(people)
    temp = deque(people)
    while temp:
        if len(temp) >= 2:
            if temp[-1] + 40 > limit:
                temp.pop()
                cnt += 1
            elif temp[0] + temp[-1] <= limit:
                temp.pop()
                temp.popleft()
                cnt += 1
        else:
            temp.pop()
            cnt += 1

    return cnt

people = [70, 50, 80, 50]
limit = 100

people2 = [70, 80, 50]

print(solution(people, limit))
print(solution(people2, limit))
