# Time: O(n) Space: O(n)
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = defaultdict(int)
        for c in s:
            charCount[c] += 1
        
        index = -1
        for c, freq in charCount.items():
            if freq == 1:
                if index == -1:
                    index = s.index(c)
                else:
                    index = min(index, s.index(c))
        
        return index