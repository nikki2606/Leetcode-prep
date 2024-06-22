# Time: O(nlogn) Space: O(n)
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        charCount = defaultdict(int)

        for char in s:
            charCount[char] += 1
        
        charCount = dict(sorted(charCount.items(), key=lambda x:x[1], reverse=True))

        res = ""
        for char, freq in charCount.items():
            while freq:
                res += char
                freq -= 1
        
        return res