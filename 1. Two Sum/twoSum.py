class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexDict = {}
        for i, num in enumerate(nums):
            if target-num in numIndexDict:
                return [i, numIndexDict[target-num]]
            numIndexDict[num] = i
        return [-1,-1]

### Notes
# Time: O(n)
# Space: O(n)