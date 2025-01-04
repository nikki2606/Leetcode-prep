class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
            
        arrCopy = arr[:]
        arr.sort()
        rankDict = {}
        rank = 1
        for num in arr:
            if num not in rankDict:
                rankDict[num] = rank
                rank += 1
        res = []
        n = len(arr)
        for i in range(n):
            res.append(rankDict[arrCopy[i]])
        return res