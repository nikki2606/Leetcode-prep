class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time: O(n)
        out = 0
        for num in nums:
            out ^= num
            
        return out