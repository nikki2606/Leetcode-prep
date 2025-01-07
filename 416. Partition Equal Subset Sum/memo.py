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
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        memo = [[-1]*(target+1) for i in range(len(nums)+1)]

        def dfs(i, target):
            if target == 0:
                return True
                
            if i >= len(nums) or target < 0:
                return False

            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dfs(i+1, target-nums[i]) or dfs(i+1, target)

            return memo[i][target]

        return dfs(0, target)

# Time: O(n*target)
# Space: O(n*target)