import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        oneD = []
        for row in matrix:
            for num in row:
                oneD.append(num)
        
        heapq.heapify(oneD)
        out = 0
        while k:
            out = heapq.heappop(oneD)
            k -= 1
        return out
# Time: O(NlogN)