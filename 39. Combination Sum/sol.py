class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, path, amount, res):
            if amount == 0:
                res.append(path[:])
                return
            elif amount < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, amount-candidates[i], res)
                path.pop()

        res = []
        candidates.sort()
        dfs(0, [], target, res)
        return res