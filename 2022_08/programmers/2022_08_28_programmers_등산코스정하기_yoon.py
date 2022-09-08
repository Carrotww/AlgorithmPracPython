from collections import defaultdict
import copy


def solution(n, paths, gates, summits):
    intensity = [0 if n + 1 in gates else 100000000 for n in range(n)]

    map_info = defaultdict(dict)
    for path in paths:
        map_info[path[0]][path[1]] = path[2]
        map_info[path[1]][path[0]] = path[2]

    origin = set(gates)
    destination = set(summits)

    candidates = copy.deepcopy(gates)
    while candidates:
        next_candidates = set()
        stack = copy.deepcopy(candidates)
        while stack:
            curr_place = stack.pop()
            for next_place, cost in map_info[curr_place].items():
                max_intensity = max(intensity[curr_place - 1], cost)
                if intensity[next_place - 1] > max_intensity:
                    intensity[next_place - 1] = max_intensity
                    if next_place not in destination and next_place not in origin:
                        next_candidates.add(next_place)
        candidates = list(next_candidates)

    result = []
    for d in destination:
        result.append([d, intensity[d - 1]])
    result.sort(key=lambda x: (x[1], x[0]))

    return result[0]
