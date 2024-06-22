class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countVecS = [0]*26
        countVecT = [0]*26

        for c in s:
            countVecS[ord(c)-ord('a')] += 1
        
        for c in t:
            countVecT[ord(c)-ord('a')] += 1

        if countVecS == countVecT:
            return True
        return False
    
### Notes
# Time: O(n)
# Space: O(1)