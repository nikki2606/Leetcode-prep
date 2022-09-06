class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cvecS = [0]*26
        cvecT = [0]*26
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            cvecS[ord(s[i])-ord('a')] += 1
            cvecT[ord(t[i])-ord('a')] += 1
        
        if cvecS == cvecT:
            return True
        return False

### Notes
# Time: O(n)
# Space: O(1)