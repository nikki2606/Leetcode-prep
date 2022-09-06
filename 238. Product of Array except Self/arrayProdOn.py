class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        An = [1]*n
        Bn = [1]*n
        res = []
        
        for i in range(1,n):
            An[i] = An[i-1]*nums[i-1]
            
        for i in range(n-2,-1,-1):
            Bn[i] = Bn[i+1]*nums[i+1]
            
        for i in range(n):
            res.append(An[i]*Bn[i])
        return res

### Notes
# Time: O(n)
# Space: O(n)