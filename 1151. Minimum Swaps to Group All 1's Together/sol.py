class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        currOnes = 0
        start = 0
        maxOnes = 0
        for i in range(len(data)):
            currOnes += data[i]
            if i-start+1 > ones:
                currOnes -= data[start]
                start += 1
            maxOnes = max(maxOnes, currOnes)
        return ones-maxOnes