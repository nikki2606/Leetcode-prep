from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charcount = Counter(s)
        res = float('inf')
        for char, freq in charcount.items():
            if freq == 1:
                res = min(res,s.index(char))
        return res if res != float('inf') else -1