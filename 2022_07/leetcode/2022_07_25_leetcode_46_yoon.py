class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # itertools 이용하는 방식
        # return itertools.permutations(nums,len(nums))

        # DFS이용하는 방식
        def dfs(stack):
            if len(stack) == len(nums):
                answer.append(copy.deepcopy(stack))
                return

            for idx in range(len(nums)):
                if visited[idx] == 0:
                    visited[idx] = 1
                    stack.append(nums[idx])
                    dfs(stack)
                    stack.pop()
                    visited[idx] = 0

        answer = []
        visited = [0 for _ in range(len(nums))]
        dfs([])

        return answer