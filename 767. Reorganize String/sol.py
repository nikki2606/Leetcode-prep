# Time: O(n) Space: O(n)
import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        charDict = {}
        maxCount = 0
        for char in s:
            if char not in charDict:
                charDict[char] = 0
            charDict[char] += 1
        maxCount = max(list(charDict.values()))
        maxCountPos = list(charDict.values()).index(maxCount)
        letter = list(charDict.keys())[maxCountPos]
        if maxCount > math.ceil(len(s)/2):
            return ""
        
        res = [""]*len(s)
        pos = 0
        while charDict[letter] != 0:
            res[pos] = letter
            pos += 2
            charDict[letter] -= 1
        
        for char, coun in charDict.items():
            while coun > 0:
                if pos >= len(s):
                    pos = 1
                res[pos] = char
                pos += 2
                coun -= 1
        
        return "".join(res)