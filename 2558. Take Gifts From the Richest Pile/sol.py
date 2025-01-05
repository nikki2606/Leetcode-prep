from heapq import heappush, heappop, heapify
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        if not gifts:
            return 0
        
        gifts = [-x for x in gifts]
        heapify(gifts)

        while k:
            k -= 1
            val = -heappop(gifts)
            heappush(gifts, -int(sqrt(val)))
        
        return -sum(gifts)