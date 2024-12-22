class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, res):
            res.append(path[:])
            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]], res)

        res = []
        dfs(0, [], res)
        return res
    # Time : O(2**n)