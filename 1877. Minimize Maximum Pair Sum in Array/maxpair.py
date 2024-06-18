# Time: O(nlogn) Space: O(1)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        nums = sorted(nums)
        res = 0
        while left < right:
            pairSum = nums[left] + nums[right]
            res = max(res, pairSum)
            left += 1
            right -= 1

        return res