# Time: O(n) Space: O(n)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) < 2:
            return -1

        maxLen = -1
        indexDict = {}

        for i,c in enumerate(s):
            if c not in indexDict:
                indexDict[c] = []
            indexDict[c].append(i)
        
        for c, freq in indexDict.items():
            if len(freq) > 1:
                maxLen = max(maxLen, freq[-1]-freq[0]-1)
            
        return maxLen