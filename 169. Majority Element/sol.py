from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = Counter(nums)
        n = len(nums)
        for num, freq in countDict.items():
            if freq > n//2:
                return num
        return nums[0]