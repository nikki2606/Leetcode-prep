# Time: O(n) Space: O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        countDict = {}
        for num in nums:
            if num not in countDict:
                countDict[num] = 0
            countDict[num] += 1

        res = 0
        for num, freq in countDict.items():
            if freq > 1:
                res += self.goodPairForNum(freq)
        
        return res

    def goodPairForNum(self, freq):
        numOfPairs = 0
        for i in range(freq,0,-1):
            numOfPairs += (i-1)
        
        return numOfPairs