class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k == 0:
            return float(0)

        n = len(nums)
        if n < k:
            return float(0)
        
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        
        maxSum = currSum
        for i in range(k,n):
            currSum += nums[i]-nums[i-k]
            maxSum = max(maxSum, currSum)
        
        return maxSum/k