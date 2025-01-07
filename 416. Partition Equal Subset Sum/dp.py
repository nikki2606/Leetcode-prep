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
        memo = set([0])
        for num in nums:
            temp = memo.copy()
            for dig in temp:
                memo.add(num+dig)
        
        return target in memo