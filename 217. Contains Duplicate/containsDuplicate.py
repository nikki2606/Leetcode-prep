class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
### Notes
# Time: O(n)
# Space: O(n)