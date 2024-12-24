class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums = [1,2,3,4]
        left_mul = [1,1,2,6]
        right_mul = [24,12,4,1]
        res = [24,12,8,6]
        '''
        n = len(nums)
        left_mul = [1]*n
        right_mul = [1]*n
        res = [1]*n
        for i in range(1,n):
            left_mul[i] = left_mul[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            right_mul[j] = right_mul[j+1]*nums[j+1]

        for i in range(n):
            res[i] = left_mul[i]*right_mul[i]
        return res