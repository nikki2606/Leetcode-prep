class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
               0 target = 11, i = 0
              / \
              1.  0
target = 10,i =1.   target=11, i = 1
          i == len(nums), target = 0 should be true, else false
          target < 0, false
        '''

        def dfs(i, target):
            if i > len(nums)-1:
                return target == 0
            if target < 0:
                return False
            
            return dfs(i+1, target-nums[i]) or dfs(i+1, target)
        
        if sum(nums)%2:
            return False
        
        return dfs(0, sum(nums)//2)

# TLE
# Time: O(2^n)
# Space: O(n)