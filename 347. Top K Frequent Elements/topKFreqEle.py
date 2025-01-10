from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num,freq in numCount.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1, -1 ,-1):
            if not bucket[i]:
                continue
            
            m = len(bucket[i])
            if k <= m:
                res.extend(bucket[i][:k])
                break
            else:
                res.extend(bucket[i])
                k -= m
        return res