from collections import defaultdict

def solution(n, number):

    def fun1(set1, set2):
        temp = set()
        for i in set1:
            for j in set2:
                temp.add(i + j)
                temp.add(i * j)
                temp.add(j - i)
                temp.add(i - j)
                if j != 0: temp.add(i // j)
                if i != 0: temp.add(j // i)
        return temp # 입력받은 두 개의 set 을 모두 계산하여서 temp 에 저장
    
    temp = defaultdict(set)
    
    for i in range(1, 10):
        if i == 1:
            temp[i].add(n)
        else:
            str_append = int(str(n) * i)
            temp[i].add(str_append)
            for x in range(1, i):
                for y in range(1, i):
                    if x + y == i:
                        temp_result = fun1(temp[x], temp[y])
                        for re in temp_result:
                            temp[i].add(re)
        if number in temp[i]:
            return i
    return -1

print(solution(5, 12))
print(solution(2, 11))