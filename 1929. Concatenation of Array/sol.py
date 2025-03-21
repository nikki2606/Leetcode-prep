class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [0]*(2*n)
        for i in range(n):
            res[i] = res[i+n] = nums[i]
        return res
    
# Time: O(n), one-pass