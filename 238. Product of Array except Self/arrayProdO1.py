class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #O(n) time O(1) space
        n = len(nums)
        An = [1]*n
        
        for i in range(1,n):
            An[i] = An[i-1]*nums[i-1]
        
        Bn = 1
        for i in range(n-1,-1,-1):
            An[i] = An[i]*Bn
            Bn = Bn * nums[i]
            
        return An