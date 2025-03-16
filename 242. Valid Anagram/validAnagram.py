class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countvecS = [0]*26
        countvecT = [0]*26
        for char in s:
            countvecS[ord(char)-ord('a')] += 1

        for char in t:
            countvecT[ord(char)-ord('a')] += 1
            
        return countvecS == countvecT

# Time: O(n+m)
# Space: O(1) coz at most 26 chars