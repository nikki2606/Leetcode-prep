from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m = len(mat)
        n = len(mat[0])

        arrDict = defaultdict(list)
        minVal, maxVal = 0, 0
        for i in range(m):
            for j in range(n):
                idxSum = i+j
                maxVal = max(maxVal, idxSum)
                arrDict[idxSum].append(mat[i][j])
        
        res = []
        for a in range(minVal, maxVal+1):
            if a%2:
                res.extend(arrDict[a])
            else:
                while arrDict[a]:
                    res.append(arrDict[a].pop())
        return res
 