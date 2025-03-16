class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if not strs:
            return [[]]
        
        ana = {}
        for s in strs:
            countvecS = self.getCountVec(s)
            if countvecS not in ana:
                ana[countvecS] = []
            ana[countvecS].append(s)
        
        for cvec, lst in ana.items():
            res.append(lst)
        
        return res

    def getCountVec(self, s):
        countvec = [0]*26
        for char in s:
            countvec[ord(char)-ord('a')] += 1
        return tuple(countvec)
    
    # Time: O(n*k)
    # Space: O(n*k)