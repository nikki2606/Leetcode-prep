class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n) Space: O(1)
        n = len(nums)
        sumOfN = n*(n+1)//2
        for num in nums:
            sumOfN -= num
        return sumOfN