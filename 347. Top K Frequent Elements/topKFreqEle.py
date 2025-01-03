from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort O(n)
        numCount = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num,freq in numCount.items():
            bucket[freq].append(num)
        res = []
        for bket in bucket:
            for num in bket:
                res.append(num)
        res = res[::-1]
        return res[:k]