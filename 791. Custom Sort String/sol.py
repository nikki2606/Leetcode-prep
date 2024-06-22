# Time: O(n) Space: O(n)
from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charDict = defaultdict(int)

        for char in s:
            charDict[char] += 1

        res = ""
        for ch in order:
            if ch in charDict:
                res += ch*charDict[ch]
                charDict[ch] = 0

        for ch, freq in charDict.items():
            if freq != 0:
                res += ch*charDict[ch]
        return res