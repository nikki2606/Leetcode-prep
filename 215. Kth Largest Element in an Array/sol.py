import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        
        out = 0
        while k:
            k -= 1
            out = heapq.heappop(h)
        return -out
# Time: O(NlogN)