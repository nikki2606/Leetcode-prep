# Time: O(n+m) Space: O(n+m)
from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        countDict = defaultdict(int)

        for num in nums:
            countDict[num] += 1
        
        res = []
        for num, freq in countDict.items():
            while len(res) < freq:
                res.append([])
            
            for i in range(freq):
                res[i].append(num)
        
        return res