from typing import List

def solution(lines):
    log_line = [[a, b, c] for a, b, c in [x.split() for x in lines]]
    end_time = [total_time(x) for x in log_line]
    start_time = [makestart_time(x) for x in log_line]
    result = 0

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]

        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        result = max(result, cnt)
    return result

def total_time(line: List) -> float:
    log_Hour = int(line[1].split(":")[0])
    log_min = int(line[1].split(":")[1])
    log_sec = float(line[1].split(":")[2])
    return int((log_sec + (log_min * 60) + (log_Hour * 3600)) * 1000)

def makestart_time(line: List) -> int:
    return int(total_time(line) - float(line[2].split('s')[0]) * 1000) + 1

li = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(li))