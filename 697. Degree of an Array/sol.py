# Time: O(n) Space: O(n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        countDict = {}
        for num in nums:
            if num not in countDict:
                countDict[num] = 0
            countDict[num] += 1
        
        degree = max(list(countDict.values()))
        degreeNum = set()

        for num,freq in countDict.items():
            if freq == degree:
                degreeNum.add(num)
        
        indices = {}
        for i,num in enumerate(nums):
            if num in degreeNum:
                if num not in indices:
                    indices[num] = []
                indices[num].append(i)
        
        res = 50000
        for num, index in indices.items():
            res = min(res, index[-1]-index[0]+1)
        
        return res