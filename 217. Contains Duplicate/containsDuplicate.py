class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ele = set()
        for num in nums:
            if num in ele:
                return True
            
            ele.add(num)
        return False

### Notes
# Time: O(n)
# Space: O(n)