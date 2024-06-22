# Time: O(n) Space: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        isoDict = {}
        for i,c in enumerate(s):
            if c not in isoDict:
                isoDict[c] = t[i]
            else:
                if isoDict[c] != t[i]:
                    return False
        
        return True