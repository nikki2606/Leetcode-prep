class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        firstPos = 0
        posFlag = 0
        for i in range(n):
            if nums[i] >= 0:
                posFlag = 1
                firstPos = i
                break

        if not posFlag:
            nums = nums[::-1]
            
        if firstPos == 0:
            return [nums[i]**2 for i in range(n)]

        neg = firstPos-1
        j = 0
        while j < n:
            if firstPos < n and neg > -1:
                if abs(nums[neg]) < nums[firstPos]:
                    res[j] = nums[neg]**2
                    neg -= 1
                else:
                    res[j] = nums[firstPos]**2
                    firstPos += 1
            elif firstPos < n:
                res[j] = nums[firstPos]**2
                firstPos += 1
            else:
                res[j] = nums[neg]**2
                neg -= 1
            j += 1
        
        return res