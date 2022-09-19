class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # itertools이용해서 풀기
        # num_list = [i for i in range(1, n+1)]
        # return itertools.combinations(num_list, k)

        # DFS 이용해서 풀기
        def dfs(stack, start):
            if len(stack) == k:
                result.append(copy.deepcopy(stack))
                return
            for idx in range(start, n):
                if visited[idx] == 0:
                    visited[idx] = 1
                    stack.append(num_list[idx])
                    dfs(stack, idx + 1)
                    stack.pop()
                    visited[idx] = 0

        result = []
        num_list = [i for i in range(1, n + 1)]
        visited = [0 for _ in range(n)]
        dfs([], 0)
        return result