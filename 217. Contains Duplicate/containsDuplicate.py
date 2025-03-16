class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        return len(nums) != len(set(nums))

# Time: O(n)