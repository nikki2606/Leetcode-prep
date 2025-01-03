class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        # prefix sum
        prefixDict = {}
        count = 0
        for num in nums:
            total += num
            if total == k:
                count += 1
            
            if total-k in prefixDict:
                count += prefixDict[total-k]
            
            if total not in prefixDict:
                prefixDict[total] = 0
            prefixDict[total] += 1

        return count