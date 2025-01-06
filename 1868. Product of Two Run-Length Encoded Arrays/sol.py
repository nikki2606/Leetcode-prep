class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        product = 1
        freq = 0
        while i < len(encoded1) and j < len(encoded2):
            product = encoded1[i][0]*encoded2[j][0]
            freq = min(encoded1[i][1], encoded2[j][1])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if encoded1[i][1] == 0:
                i += 1

            if encoded2[j][1] == 0:
                j += 1
            
            if not res or res[-1][0] != product:
                res.append([product,freq])
            else:
                res[-1][1] += freq
        
        return res