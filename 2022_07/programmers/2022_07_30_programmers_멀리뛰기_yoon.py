import math

def solution(n):
    def cal_combination(_one_num, _two_num):
        _total = _one_num + _two_num
        return (check_factorial(_total)) // (check_factorial(_one_num) * check_factorial(_two_num))

    def check_factorial(_num):
        if _num in factorial_dict:
            return factorial_dict[_num]
        else:
            tmp_num = math.factorial(_num)
            factorial_dict[_num] = tmp_num
            return tmp_num

    factorial_dict = dict()
    one_num_possible = [n1 for n1 in range(n, -1, -2)]
    two_num_possible = [n2 // 2 for n2 in range(0, n + 1, 2)]

    result = 0
    for one_num, two_num in zip(one_num_possible, two_num_possible):
        result += cal_combination(one_num, two_num)

    return result % 1234567