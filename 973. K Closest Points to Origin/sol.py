import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            d = self.distance(x,y)
            heapq.heappush(h, (d, [x,y]))
        
        res = []
        while k:
            out = heapq.heappop(h)
            res.append(out[-1])
            k -= 1
        return res

    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)