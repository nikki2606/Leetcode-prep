from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        h = []
        for num, freq in numCount.items():
            heappush(h, (-freq, num))
        res = []
        while k:
            k -= 1
            val = heappop(h)
            res.append(val[1])
        return res