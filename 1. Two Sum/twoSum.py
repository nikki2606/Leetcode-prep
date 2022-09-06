class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            b = target - nums[i]
            if b in d:
                return [d[b],i]
            d[nums[i]] = i
            
        return [-1,-1]

### Notes
# Time: O(n)
# Space: O(n)