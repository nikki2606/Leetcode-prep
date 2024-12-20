class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [0]*n

        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return

            for i, num in enumerate(nums):
                if visited[i]:
                    continue

                path.append(num)
                visited[i] = 1
                dfs(start+1, path)
                visited[i] = 0
                path.pop()

        dfs(0, [])
        return res