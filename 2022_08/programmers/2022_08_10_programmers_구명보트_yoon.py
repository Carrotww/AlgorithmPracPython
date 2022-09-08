from collections import deque
def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    result = 0
    while people:
        if len(people) <= 1:
            break
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            result += 1
        else:
            people.popleft()
            result += 1

    if people:
        return result + 1
    return result