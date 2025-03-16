class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        indices = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in indices:
                return [indices[b], i]
            indices[nums[i]] = i
        return [-1, -1]

# Time : O(n)
# Space: O(n)