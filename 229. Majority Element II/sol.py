class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = []
        maxFreqEle1 = None
        maxFreq1 = 0
        maxFreqEle2 = None
        maxFreq2 = 0
        n = len(nums)

        for num in nums:
            if maxFreqEle1 == num:
                maxFreq1 += 1
            elif maxFreqEle2 == num:
                maxFreq2 += 1
            elif maxFreq1 == 0:
                maxFreqEle1 = num
                maxFreq1 += 1
            elif maxFreq2 == 0:
                maxFreqEle2 = num
                maxFreq2 += 1
            else:
                maxFreq1 -= 1
                maxFreq2 -= 1
        
        for num in [maxFreqEle1, maxFreqEle2]:
            if nums.count(num) > n//3:
                res.append(num)
        return res