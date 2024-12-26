from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        charcount = Counter(s)
        n = len(s)
        h = []
        for char, count in charcount.items():
            if count > (n+1)//2:
                return ""
            heapq.heappush(h, (-count, char))
        
        res = [None]*n
        pointer = 0
        while h:
            coun, char = heapq.heappop(h)
            coun = -coun
            while coun:
                res[pointer] = char
                pointer += 2
                if pointer >= n:
                    pointer = 1
                coun -= 1
        return "".join(res)
    # Time: O(NlogN)