def solution(lines):
    def date_to_milsec(_date_string):
        _date_string = _date_string.split(".")
        _date_HMS = _date_string[0].split(":")
        return_milsec = 0
        return_milsec += int(_date_HMS[0]) * 3600 * 1000
        return_milsec += int(_date_HMS[1]) * 60 * 1000
        return_milsec += int(_date_HMS[2]) * 1000
        return_milsec += int(_date_string[1])
        return return_milsec

    def get_traffic(_check_start, _check_end):
        _traffic = 0
        for _s, _e in start_end_pair:
            if _check_end > _s and _check_start <= _e:
                _traffic += 1
        return _traffic

    result = -1
    start_end_pair = []
    for line in lines:
        tmp = line.split()
        tmp_end_time = date_to_milsec(tmp[1])
        tmp_duration = int(float(tmp[2].replace("s", "")) * 1000)
        start_end_pair.append([tmp_end_time - tmp_duration + 1, tmp_end_time])
    print(start_end_pair)

    for start_time, end_time in start_end_pair:
        result = max(result, get_traffic(start_time, start_time + 1000), get_traffic(end_time, end_time + 1000))

    return result