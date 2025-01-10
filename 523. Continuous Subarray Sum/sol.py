from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumDict = defaultdict(int)
        sumDict[0] = -1
        sum = 0
        for i,num in enumerate(nums):
            sum += num
            check = sum%k
            if check not in sumDict:
                sumDict[check] = i
            elif i - sumDict[check] > 1:
                return True
        return False