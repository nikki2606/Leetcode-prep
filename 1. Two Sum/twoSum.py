class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        numDict = {}
        for i in range(len(nums)):
            if target-nums[i] in numDict:
                return [numDict[target-nums[i]], i]
            numDict[nums[i]] = i
        
        return [-1,-1]