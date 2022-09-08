class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates.sort()

        def get_result(comb, value, condition):
            if value < 0:
                return;
            if value == 0:
                result.add(tuple(comb))
            for idx, c in enumerate(candidates):
                if idx < condition:
                    continue
                tmp = comb[:]
                tmp.append(c)
                get_result(tmp, value - c, idx)

        get_result([], target, 0)
        return list(map(list, result))