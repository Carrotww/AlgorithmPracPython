#내풀이
from collections import defaultdict


def solution(files):
    def to_lower(s):
        s.lower()
        return s

    split_dict = defaultdict(list)
    result = []

    for file in files:
        check = 0
        tmp_split = ["", "", ""]
        for f_c in file:
            if check == 0 and f_c.isdigit():
                check += 1
            elif check == 1 and not f_c.isdigit():
                check += 1

            tmp_split[check] += f_c
        split_key = tmp_split[0]
        split_dict[split_key.lower()].append(tmp_split)
    for v in split_dict.values():
        v.sort(key=lambda x: int(x[1]))
    for k in sorted(split_dict.keys()):
        result.extend(list(map(''.join, split_dict[k])))
    return result