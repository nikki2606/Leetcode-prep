from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram = {}
        for w in strs:
            wDict = defaultdict(int)
            for c in sorted(w):
                wDict[c] += 1

            tupleDict = tuple(wDict.items())
            if tupleDict not in anagram:
                anagram[tupleDict] = []
            anagram[tupleDict].append(w)
        
        for k,v in anagram.items():
            res.append(v)
        
        return res

### Notes
# Time: O(n)
# Space: O(n)