class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSum = nums[0]
        minSum = nums[0]
        currSum = 0
        currMin = 0
        totalSum = 0

        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)

            currMin = min(currMin + num, num)
            minSum = min(minSum, currMin)

            totalSum += num
        
        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum-minSum)
# Kadane algorithm