# Time: O(n) Space: O(n)
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        revDict = {}

        for num in nums:
            ans = num - self.rev(num)
            if ans not in revDict:
                revDict[ans] = []
            revDict[ans].append(num)

        res = 0

        for ans, pair in revDict.items():
            if len(pair) > 1:
                res += self.sumPair(len(pair))
        
        return res%(10**9 + 7)

    def rev(self, x):
        num = 0
        it = 0
        y = x
        while y > 0:
            it += 1
            y = y//10

        while x > 0:
            r = x%10
            num += r*(10**(it-1))
            it -= 1
            x = x//10
        return num

    def sumPair(self, n):
        total = 0
        for i in range(1,n):
            total += i
        return total